from datetime import datetime, timezone

from fastapi import APIRouter, Depends, Header, HTTPException, Query
from sqlalchemy import select
from sqlalchemy.orm import Session

from database.database import engine, get_db
from database.schema_guard import ensure_lesson_columns
from models.game import Game
from models.game_event import GameEvent
from models.game_session import GameSession
from models.lesson import Lesson
from models.user import User
from schemas.game import GameEventCreate, GameSessionCreate

router = APIRouter(prefix="/games", tags=["games"])

try:
    ensure_lesson_columns(engine)
except Exception:
    pass


def _resolve_or_create_user(
    db: Session,
    raw_user_id: int | str | None,
    firebase_uid: str | None,
    user_name: str | None,
) -> User:
    uid = (firebase_uid or "").strip()
    if not uid and isinstance(raw_user_id, str) and not raw_user_id.isdigit():
        uid = raw_user_id.strip()

    if uid:
        user = db.scalar(select(User).where(User.firebase_uid == uid))
        if user is None:
            uname = f"fb_{uid[:48]}"
            user = db.scalar(select(User).where(User.username == uname))
            if user is None:
                user = User(
                    username=uname,
                    firebase_uid=uid,
                    password_hash="firebase",
                    name=(user_name or "Người chơi")[:100],
                )
                db.add(user)
                db.commit()
                db.refresh(user)
            elif not user.firebase_uid:
                user.firebase_uid = uid
                db.commit()
        return user

    numeric_id = None
    if isinstance(raw_user_id, int):
        numeric_id = raw_user_id
    elif isinstance(raw_user_id, str) and raw_user_id.isdigit():
        numeric_id = int(raw_user_id)

    if numeric_id and numeric_id > 0:
        user = db.get(User, numeric_id)
        if user is not None:
            return user

    guest = db.scalar(select(User).where(User.username == "guest_player"))
    if guest is None:
        guest = User(
            username="guest_player",
            password_hash="guest",
            name="Khách trải nghiệm",
        )
        db.add(guest)
        db.commit()
        db.refresh(guest)
    return guest


def _resolve_game(db: Session, payload: GameSessionCreate) -> Game | None:
    if payload.game_id:
        game = db.get(Game, payload.game_id)
        if game is not None:
            return game

    if payload.lesson_id:
        game = db.scalar(select(Game).where(Game.lesson_id == payload.lesson_id))
        if game is not None:
            return game
        lesson = db.get(Lesson, payload.lesson_id)
        if lesson is not None:
            gtype = payload.game_key or payload.game_type or lesson.game_type or "simulation"
            game = Game(
                lesson_id=lesson.id,
                title=(lesson.game_title or lesson.title)[:200],
                description=lesson.game_description,
                game_type=gtype[:100],
            )
            db.add(game)
            db.commit()
            db.refresh(game)
            return game

    return None


@router.post("/sessions")
def create_session(
    payload: GameSessionCreate,
    db: Session = Depends(get_db),
    x_firebase_uid: str | None = Header(default=None, alias="X-Firebase-Uid"),
):
    game = _resolve_game(db, payload)
    if game is None:
        raise HTTPException(status_code=404, detail="Game not found")

    uid = payload.firebase_uid or x_firebase_uid
    user = _resolve_or_create_user(db, payload.user_id, uid, payload.user_name)

    session = GameSession(
        user_id=user.id,
        game_id=game.id,
    )
    db.add(session)
    db.commit()
    db.refresh(session)

    return {
        "id": session.id,
        "user_id": session.user_id,
        "firebase_uid": user.firebase_uid,
        "game_id": session.game_id,
        "started_at": session.started_at,
        "score": session.score,
    }


@router.post("/sessions/{session_id}/events")
def add_event(
    session_id: int,
    payload: GameEventCreate,
    db: Session = Depends(get_db),
):
    session = db.get(GameSession, session_id)
    if session is None:
        raise HTTPException(status_code=404, detail="Game session not found")

    event = GameEvent(
        session_id=session_id,
        action=payload.action,
        event_data=payload.event_data,
    )
    db.add(event)
    db.commit()
    db.refresh(event)
    return {"id": event.id, "status": "recorded"}


@router.post("/sessions/{session_id}/finish")
def finish_session(
    session_id: int,
    score: int | None = Query(default=None, ge=0, le=10000),
    db: Session = Depends(get_db),
):
    session = db.get(GameSession, session_id)
    if session is None:
        raise HTTPException(status_code=404, detail="Game session not found")

    if session.finished_at is not None:
        raise HTTPException(status_code=409, detail="Game session already finished")

    session.finished_at = datetime.now(timezone.utc)
    session.score = score
    db.commit()
    return {"status": "finished", "session_id": session.id, "score": score}
