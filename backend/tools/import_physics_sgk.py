"""Nhập nội dung Vật lý lớp 6–12 theo SGK "Kết nối tri thức với cuộc sống".

Mỗi bài học = 1 chủ đề (lớp 1–5) / 1 chương (lớp 6–12) được đánh số trong SGK,
xếp đúng thứ tự mục lục. Dữ liệu nằm trong backend/tools/physics_sgk/lopN.py.

Script sẽ: kiểm tra dữ liệu -> bổ sung cột mới (requirements, quiz) nếu thiếu
-> XOÁ các bài Vật lý cũ của những lớp được chọn -> chèn bài mới.

Cách dùng (chạy trong thư mục backend):
    python tools/import_physics_sgk.py --grades 6 --dry-run      # chỉ kiểm tra dữ liệu
    python tools/import_physics_sgk.py --grades 6                # ghi vào CSDL trong .env
    python tools/import_physics_sgk.py --grades 6-12 --write-catalog
    python tools/import_physics_sgk.py --grades 6 --db-url sqlite:///./thu.db
"""
import argparse
import copy
import importlib
import json
import os
import random
import sys
from pathlib import Path

BACKEND_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BACKEND_DIR))
sys.path.insert(0, str(BACKEND_DIR / "tools"))

LEVEL_PLAN = {
    # mức: (số câu trắc nghiệm, số câu đúng/sai, số câu trả lời ngắn)
    "biet": (4, 0, 0),
    "hieu": (2, 2, 0),
    "vandung": (1, 0, 1),
}
LEVEL_ORDER = ["biet", "hieu", "vandung"]
REQUIRED_TEXT = ("topic", "title", "description", "definition", "theory", "example", "example_answer", "real_life")


def parse_grades(text: str) -> list[int]:
    import re
    grades: set[int] = set()
    for part in text.split(','):
        part = part.strip().strip('\/\'\"')
        if not part:
            continue
        if '-' in part:
            a, b = part.split('-', 1)
            a_num = re.sub(r'\D', '', a)
            b_num = re.sub(r'\D', '', b)
            if a_num and b_num:
                grades.update(range(int(a_num), int(b_num) + 1))
        else:
            p_num = re.sub(r'\D', '', part)
            if p_num:
                grades.add(int(p_num))
    bad = [g for g in grades if g < 6 or g > 12]
    if bad:
        raise SystemExit(f"Lớp không hợp lệ: {bad} (chỉ hỗ trợ 6–12)")
    return sorted(grades)


def load_grade(grade: int) -> list[dict]:
    return importlib.import_module(f"physics_sgk.lop{grade}").LESSONS


def validate_lesson(grade: int, idx: int, lesson: dict) -> list[str]:
    errs: list[str] = []
    tag = f"Lớp {grade} · bài {idx + 1} ({lesson.get('topic', '?')})"
    for key in REQUIRED_TEXT:
        if not str(lesson.get(key) or "").strip():
            errs.append(f"{tag}: thiếu '{key}'")
    if len(lesson.get("topic", "")) > 150 or len(lesson.get("title", "")) > 200:
        errs.append(f"{tag}: topic/title quá dài")
    if lesson.get("icon") and len(lesson["icon"]) > 20:
        errs.append(f"{tag}: icon quá dài")
    if not lesson.get("requirements"):
        errs.append(f"{tag}: thiếu Yêu cầu cần đạt")
    formulas = lesson.get("formulas") or []
    if not formulas or not all(g.get("items") for g in formulas):
        errs.append(f"{tag}: thiếu công thức/quy tắc")
    for g in formulas:
        for it in g.get("items", []):
            if not it.get("name") or not it.get("formula"):
                errs.append(f"{tag}: công thức thiếu name/formula trong nhóm '{g.get('category')}'")

    quiz = lesson.get("quiz") or []
    if len(quiz) != 10:
        errs.append(f"{tag}: cần đúng 10 câu, đang có {len(quiz)}")
    tf_type = "tf" if grade <= 5 else "tf4"
    levels = [q.get("level") for q in quiz]
    if levels != sorted(levels, key=lambda l: LEVEL_ORDER.index(l) if l in LEVEL_ORDER else 99):
        errs.append(f"{tag}: các câu chưa xếp theo thứ tự Biết → Hiểu → Vận dụng")
    for level, plan in LEVEL_PLAN.items():
        qs = [q for q in quiz if q.get("level") == level]
        got = (sum(q.get("type") == "mcq" for q in qs), sum(q.get("type") == tf_type for q in qs),
               sum(q.get("type") == "short" for q in qs))
        if got != plan or len(qs) != sum(plan):
            errs.append(f"{tag}: mức '{level}' cần {plan[0]} TN + {plan[1]} {tf_type} + {plan[2]} TLN, đang có {got}")
    for qi, q in enumerate(quiz, 1):
        qtag = f"{tag} · câu {qi}"
        if not str(q.get("q") or "").strip():
            errs.append(f"{qtag}: thiếu đề")
        if not str(q.get("solution") or "").strip():
            errs.append(f"{qtag}: thiếu lời giải")
        t = q.get("type")
        if t == "mcq":
            opts = q.get("options") or []
            if len(opts) != 4 or len({str(o).strip() for o in opts}) != 4:
                errs.append(f"{qtag}: trắc nghiệm cần 4 đáp án khác nhau")
            if not isinstance(q.get("answer"), int) or isinstance(q.get("answer"), bool) or not 0 <= q["answer"] <= 3:
                errs.append(f"{qtag}: đáp án phải là số 0–3")
        elif t == "tf":
            if not isinstance(q.get("answer"), bool):
                errs.append(f"{qtag}: đáp án Đúng/Sai phải là True/False")
        elif t == "tf4":
            st, ans = q.get("statements") or [], q.get("answer")
            if len(st) != 4 or not isinstance(ans, list) or len(ans) != 4 or not all(isinstance(a, bool) for a in ans):
                errs.append(f"{qtag}: Đúng/Sai cần 4 ý a–d (statements) và 4 đáp án True/False")
        elif t == "short":
            if not q.get("answer") or not isinstance(q.get("answer"), list):
                errs.append(f"{qtag}: trả lời ngắn cần danh sách đáp án chấp nhận")
        else:
            errs.append(f"{qtag}: loại câu không hợp lệ '{t}'")
    return errs


def balance_answers(lesson: dict) -> list[dict]:
    """Xoay vòng các phương án trắc nghiệm để đáp án đúng rải đều A/B/C/D.

    Chỉ xoay vòng (giữ nguyên thứ tự tương đối của các phương án), ngẫu nhiên
    nhưng cố định theo topic -> chạy lại nhiều lần vẫn cho cùng kết quả.
    """
    quiz = copy.deepcopy(lesson["quiz"])
    mcqs = [q for q in quiz if q["type"] == "mcq"]
    rng = random.Random("hdlg:" + lesson["topic"])
    targets = [0, 1, 2, 3] * ((len(mcqs) + 3) // 4)
    rng.shuffle(targets)
    for q, target in zip(mcqs, targets):
        k = (q["answer"] - target) % 4
        q["options"] = q["options"][k:] + q["options"][:k]
        q["answer"] = target
    return quiz


def to_row(subject_id: int, grade: int, lesson: dict) -> dict:
    lesson = dict(lesson, quiz=balance_answers(lesson))
    quiz = [{k: v for k, v in q.items() if v is not None} for q in lesson["quiz"]]
    formula_text = "\n".join(f"{it['name']}: {it['formula']}" for g in lesson["formulas"] for it in g["items"])
    first_mcq = next(q for q in lesson["quiz"] if q["type"] == "mcq")
    return dict(
        subject_id=subject_id, grade=grade, topic=lesson["topic"], title=lesson["title"],
        icon=lesson.get("icon"), description=lesson["description"], definition=lesson["definition"],
        concept=lesson.get("concept"), formulas=lesson["formulas"], meaning=lesson.get("meaning"),
        real_life=lesson["real_life"], context_title=lesson.get("context_title"), context=lesson.get("context"),
        theory=lesson["theory"], formula=formula_text, example=lesson["example"],
        example_answer=lesson["example_answer"],
        # Giữ 1 câu đơn cho các màn hình cũ (dự phòng); bộ 10 câu nằm trong `quiz`.
        question=first_mcq["q"], answers=first_mcq["options"], correct=first_mcq["answer"],
        application=lesson.get("application") or lesson["real_life"],
        challenge=lesson.get("challenge"), challenge_answer=lesson.get("challenge_answer"),
        game_title=lesson.get("game_title"), game_description=lesson.get("game_description"), game_type=lesson.get("game_type"),
        requirements=lesson["requirements"], quiz=quiz,
    )


def write_catalog() -> None:
    """Tạo lại public/lesson-catalog.json (dữ liệu dự phòng cho trợ lý)."""
    from fastapi import Response
    from database.database import SessionLocal
    from routers.content import lesson_catalog

    path = BACKEND_DIR.parent / "public" / "lesson-catalog.json"
    db = SessionLocal()
    try:
        data = [i.model_dump() for i in lesson_catalog(response=Response(), db=db)]
        path.write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
        print(f"Đã ghi {path} ({len(data)} bài)")
    finally:
        db.close()
    bump_data_version()


def bump_data_version() -> None:
    """Đổi HDLG_DATA_VERSION trong public/auth.js -> trình duyệt bỏ bản lưu tạm cũ sau khi deploy."""
    import re
    from datetime import datetime

    path = BACKEND_DIR.parent / "public" / "auth.js"
    if not path.exists():
        return
    raw = path.read_bytes().decode("utf-8")
    version = datetime.now().strftime("%Y%m%d-%H%M%S")
    new, n = re.subn(r'var HDLG_DATA_VERSION = "[^"]*";', f'var HDLG_DATA_VERSION = "{version}";', raw, count=1)
    if n:
        path.write_bytes(new.encode("utf-8"))
        print(f"Đã đổi phiên bản dữ liệu trong public/auth.js -> {version} (nhớ deploy lại)")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--grades", default="1", help="vd: 1 | 1,2,3 | 1-12")
    ap.add_argument("--db-url", help="ghi đè DATABASE_URL (vd sqlite:///./thu.db)")
    ap.add_argument("--dry-run", action="store_true", help="chỉ kiểm tra dữ liệu, không ghi CSDL")
    ap.add_argument("--write-catalog", action="store_true", help="tạo lại public/lesson-catalog.json sau khi nhập")
    ap.add_argument("--yes", action="store_true", help="không hỏi xác nhận")
    args = ap.parse_args()

    grades = parse_grades(args.grades)
    data = {g: load_grade(g) for g in grades}
    errors: list[str] = []
    for g, lessons in data.items():
        topics = [l["topic"] for l in lessons]
        if len(set(topics)) != len(topics):
            errors.append(f"Lớp {g}: topic bị trùng")
        for i, l in enumerate(lessons):
            errors.extend(validate_lesson(g, i, l))
        print(f"Lớp {g}: {len(lessons)} bài, {sum(len(l['quiz']) for l in lessons)} câu hỏi")
    if errors:
        print("\n❌ Dữ liệu chưa hợp lệ:")
        for e in errors:
            print("  -", e)
        raise SystemExit(1)
    print("✅ Dữ liệu hợp lệ.")
    if args.dry_run:
        return

    if args.db_url:
        os.environ["DATABASE_URL"] = args.db_url
    from sqlalchemy import delete, select
    from database.database import DATABASE_URL, SessionLocal, engine
    from database.schema_guard import ensure_lesson_columns
    import models  # noqa: F401
    from models.game import Game
    from models.game_event import GameEvent
    from models.game_session import GameSession
    from models.lesson import Lesson
    from models.progress import Progress
    from models.subject import Subject

    print("CSDL:", DATABASE_URL.split("@")[-1])
    if not args.yes:
        ok = input(f"Sẽ XOÁ bài Vật lý cũ lớp {grades} và nhập bài mới. Gõ 'yes' để tiếp tục: ")
        if ok.strip().lower() != "yes":
            print("Đã huỷ.")
            return

    added = ensure_lesson_columns(engine)
    if added:
        print("Đã thêm cột:", added)

    db = SessionLocal()
    try:
        subject = db.scalar(select(Subject).where(Subject.slug == "physics"))
        if subject is None:
            subject = Subject(slug="physics", name="Vật lý")
            db.add(subject)
            db.flush()
        for g in grades:
            old_ids = list(db.scalars(select(Lesson.id).where(Lesson.subject_id == subject.id, Lesson.grade == g)))
            if old_ids:
                game_ids = list(db.scalars(select(Game.id).where(Game.lesson_id.in_(old_ids))))
                if game_ids:
                    sess_ids = list(db.scalars(select(GameSession.id).where(GameSession.game_id.in_(game_ids))))
                    if sess_ids:
                        db.execute(delete(GameEvent).where(GameEvent.session_id.in_(sess_ids)))
                        db.execute(delete(GameSession).where(GameSession.id.in_(sess_ids)))
                    db.execute(delete(Game).where(Game.id.in_(game_ids)))
                db.execute(delete(Progress).where(Progress.lesson_id.in_(old_ids)))
                db.execute(delete(Lesson).where(Lesson.id.in_(old_ids)))
            for lesson in data[g]:  # chèn đúng thứ tự mục lục (id tăng dần)
                db.add(Lesson(**to_row(subject.id, g, lesson)))
                db.flush()
            print(f"Lớp {g}: xoá {len(old_ids)} bài cũ, thêm {len(data[g])} bài mới")
        db.commit()
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()

    if args.write_catalog:
        write_catalog()
    print("🎉 Hoàn tất.")


if __name__ == "__main__":
    main()
