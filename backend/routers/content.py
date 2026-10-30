from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy import select
from sqlalchemy.orm import Session

from database.database import get_db
from models.game import Game
from models.lesson import Lesson
from models.subject import Subject
from schemas.content import CatalogItem, GameOut, LessonOut, SubjectOut

router = APIRouter(prefix="/content", tags=["content"])

# Lưu đệm (Edge Cache) trên Vercel CDN 24 giờ và trên trình duyệt 10 phút để không phải đánh thức Neon DB mỗi lần bấm
EDGE_CACHE_HEADER = "public, max-age=600, s-maxage=86400, stale-while-revalidate=3600"

@router.get("/subjects", response_model=list[SubjectOut])
def list_subjects(response: Response, db: Session = Depends(get_db)):
    response.headers["Cache-Control"] = EDGE_CACHE_HEADER
    return list(db.scalars(select(Subject).order_by(Subject.id)).all())

@router.get("/subjects/{slug}", response_model=SubjectOut)
def get_subject(slug: str, response: Response, db: Session = Depends(get_db)):
    subject = db.scalar(select(Subject).where(Subject.slug == slug))
    if subject is None:
        raise HTTPException(status_code=404, detail="Subject not found")
    response.headers["Cache-Control"] = EDGE_CACHE_HEADER
    return subject

@router.get("/subjects/{slug}/lessons", response_model=list[LessonOut])
def list_lessons(
    slug: str,
    response: Response,
    grade: int | None = None,
    topic: str | None = None,
    db: Session = Depends(get_db),
):
    subject = db.scalar(select(Subject).where(Subject.slug == slug))
    if subject is None:
        raise HTTPException(status_code=404, detail="Subject not found")

    stmt = select(Lesson).where(Lesson.subject_id == subject.id)
    if grade is not None:
        stmt = stmt.where(Lesson.grade == grade)
    if topic:
        stmt = stmt.where(Lesson.topic == topic)

    response.headers["Cache-Control"] = EDGE_CACHE_HEADER
    return list(db.scalars(stmt.order_by(Lesson.id)).all())

@router.get("/catalog", response_model=list[CatalogItem])
def lesson_catalog(response: Response, db: Session = Depends(get_db)):
    """Danh mục gọn của TẤT CẢ bài học (không kèm nội dung) — vài chục KB thay vì ~1,2 MB."""
    rows = db.execute(
        select(
            Lesson.id, Subject.slug, Lesson.grade, Lesson.topic, Lesson.title, Lesson.icon,
            Lesson.game_type, Lesson.question, Lesson.answers,
        ).join(Subject, Subject.id == Lesson.subject_id).order_by(Lesson.id)
    ).all()
    response.headers["Cache-Control"] = EDGE_CACHE_HEADER
    return [
        CatalogItem(
            id=r.id, subject=r.slug, grade=r.grade, topic=r.topic, title=r.title, icon=r.icon,
            has_game=bool(r.game_type), has_quiz=bool(r.question and r.answers), game_type=r.game_type,
        )
        for r in rows
    ]

@router.get("/lessons/{lesson_id}", response_model=LessonOut)
def get_lesson(lesson_id: int, response: Response, db: Session = Depends(get_db)):
    lesson = db.get(Lesson, lesson_id)
    if lesson is None:
        raise HTTPException(status_code=404, detail="Lesson not found")
    response.headers["Cache-Control"] = EDGE_CACHE_HEADER
    return lesson

@router.get("/lessons/{lesson_id}/games", response_model=list[GameOut])
def list_lesson_games(lesson_id: int, response: Response, db: Session = Depends(get_db)):
    if db.get(Lesson, lesson_id) is None:
        raise HTTPException(status_code=404, detail="Lesson not found")
    response.headers["Cache-Control"] = EDGE_CACHE_HEADER
    return list(db.scalars(
        select(Game).where(Game.lesson_id == lesson_id).order_by(Game.id)
    ).all())
