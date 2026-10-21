import argparse
import os
import sys
from pathlib import Path

# Tự động xác định thư mục `backend/` và `backend/tools/` dù đặt file ở đâu hay chạy từ đâu
_CURRENT_DIR = Path(__file__).resolve().parent
BACKEND_DIR = _CURRENT_DIR.parent if _CURRENT_DIR.name == "tools" else _CURRENT_DIR
TOOLS_DIR = BACKEND_DIR / "tools"

for _p in (TOOLS_DIR, BACKEND_DIR):
    if _p.exists() and str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

# Chuyển working directory về `backend/` để đường dẫn SQLite tương đối (sqlite:///./...) luôn khớp với FastAPI
os.chdir(BACKEND_DIR)

try:
    from dotenv import load_dotenv
    _env_path = BACKEND_DIR / ".env"
    if _env_path.exists():
        load_dotenv(dotenv_path=_env_path, override=True)
except ImportError:
    pass

# Cho phép truyền trực tiếp chuỗi kết nối Database Online (Neon/Render) qua tham số --db-url
_pre_parser = argparse.ArgumentParser(add_help=False)
_pre_parser.add_argument("--db-url", default=None)
_pre_args, _ = _pre_parser.parse_known_args()
if _pre_args.db_url:
    _db_url = _pre_args.db_url.strip()
    if _db_url.startswith("postgres://"):
        _db_url = _db_url.replace("postgres://", "postgresql+psycopg://", 1)
    elif _db_url.startswith("postgresql://") and "+psycopg" not in _db_url and "+psycopg2" not in _db_url:
        _db_url = _db_url.replace("postgresql://", "postgresql+psycopg://", 1)
    os.environ["DATABASE_URL"] = _db_url

# Tương thích tự động kiểu JSONB của PostgreSQL khi chạy trên SQLite
try:
    from sqlalchemy.dialects.sqlite.base import SQLiteTypeCompiler
    if not hasattr(SQLiteTypeCompiler, "visit_JSONB"):
        SQLiteTypeCompiler.visit_JSONB = SQLiteTypeCompiler.visit_JSON
except Exception:
    pass

"""
Master Upgrade Script – Đồng bộ & Nâng cấp toàn bộ nội dung bài học các môn (Toán, Vật lý, Hóa học).

Toàn bộ dữ liệu chi tiết đã được hợp nhất và mở rộng hoàn chỉnh vào:
  1. `upgrade_math_1_9.py`   : 54 bài Toán Lớp 1–9 (6 bài/lớp)
  2. `upgrade_math_10_12.py` : 24 bài Toán Lớp 10–12 (8 bài/lớp)
  3. `upgrade_physics.py`    : 50 bài Vật lý Lớp 6–12 (7–8 bài/lớp)
  4. `upgrade_chemistry.py`  : 49 bài Hóa học Lớp 6–12 (7 bài/lớp)
  => Tổng cộng: 177 bài học chuẩn GDPT 2018.

Cách chạy từ thư mục backend hoặc backend/tools:
  - Nâng cấp Database hiện tại trong .env (Local):
        python upgrade_lesson_content.py
  - Nâng cấp thẳng lên Database Online (Neon / Render / Railway):
        python upgrade_lesson_content.py --db-url "postgresql://user:pass@ep-...neon.tech/neondb?sslmode=require"
"""

from sqlalchemy import select
from database.database import SessionLocal, engine
from models.lesson import Lesson
from models.subject import Subject

import upgrade_math_1_9
import upgrade_math_10_12
import upgrade_physics
import upgrade_chemistry


SUBJECT_MODULES = [
    ("math", "Toán (Lớp 1–9)", upgrade_math_1_9.LESSONS),
    ("math", "Toán (Lớp 10–12)", upgrade_math_10_12.LESSONS),
    ("physics", "Vật lý (Lớp 6–12)", upgrade_physics.LESSONS),
    ("chemistry", "Hóa học (Lớp 6–12)", upgrade_chemistry.LESSONS),
]

SUBJECT_NAMES = {
    "math": "Toán",
    "physics": "Vật lý",
    "chemistry": "Hóa học",
}


def flatten_formulas_to_strings(formulas_data):
    """Chuyển cấu trúc formulas phân nhóm [{category, items}] thành list[str] phẳng nếu schema yêu cầu list[str]."""
    if not formulas_data:
        return []
    flat = []
    for group in formulas_data:
        if isinstance(group, str):
            flat.append(group)
            continue
        if isinstance(group, dict):
            cat = group.get("category", "")
            for item in group.get("items", []):
                name = item.get("name", "")
                f_str = item.get("formula", "")
                note = item.get("note", "")
                prefix = f"[{cat}] " if cat else ""
                line = f"{prefix}{name}: {f_str}" if name else f"{prefix}{f_str}"
                if note:
                    line += f" ({note})"
                flat.append(line)
    return flat


def upsert_subject_lessons(db, subject_slug, lessons_data, grade_filter=None, flat_formulas=False):
    subject = db.scalar(select(Subject).where(Subject.slug == subject_slug))
    if subject is None:
        subject = Subject(slug=subject_slug, name=SUBJECT_NAMES.get(subject_slug, subject_slug))
        db.add(subject)
        db.flush()
        print(f"[CREATE SUBJECT] Đã tạo môn '{subject.name}' (slug={subject_slug}, id={subject.id})")

    created = 0
    updated = 0

    for item in lessons_data:
        if grade_filter is not None and item["grade"] != grade_filter:
            continue

        lesson = db.scalar(
            select(Lesson).where(
                Lesson.subject_id == subject.id,
                Lesson.grade == item["grade"],
                Lesson.topic == item["topic"],
            )
        )

        if lesson is None:
            lesson = Lesson(
                subject_id=subject.id,
                grade=item["grade"],
                topic=item["topic"],
                title=item["title"],
            )
            db.add(lesson)
            created += 1
            status = "CREATE"
        else:
            updated += 1
            status = "UPDATE"

        for key, value in item.items():
            if key == "formulas" and flat_formulas:
                value = flatten_formulas_to_strings(value)
            if hasattr(lesson, key):
                setattr(lesson, key, value)

        print(f"  [{status}] {subject_slug.upper()} | Lớp {item['grade']:>2} | {item['topic']:<32} | {item['title']}")

    return created, updated


def update_lessons(subject_filter="all", grade_filter=None, flat_formulas=False):
    print(f"[INFO] Đang kết nối Database: {engine.url.render_as_string(hide_password=True)}")
    total_created = 0
    total_updated = 0

    with SessionLocal() as db:
        try:
            for slug, label, lessons_list in SUBJECT_MODULES:
                if subject_filter != "all" and slug != subject_filter:
                    continue

                print("\n" + "-" * 72)
                print(f"ĐANG ĐỒNG BỘ: {label} ({len(lessons_list)} bài)")
                print("-" * 72)

                c, u = upsert_subject_lessons(
                    db,
                    slug,
                    lessons_list,
                    grade_filter=grade_filter,
                    flat_formulas=flat_formulas,
                )
                total_created += c
                total_updated += u

            db.commit()

            print("\n" + "=" * 72)
            print("HOÀN TẤT NÂNG CẤP TOÀN BỘ DỮ LIỆU BÀI HỌC BACKEND")
            print(f"  • Database đích     : {engine.url.render_as_string(hide_password=True)}")
            print(f"  • Tổng số bài xử lý : {total_created + total_updated} bài")
            print(f"  • Tạo mới (CREATE)  : {total_created} bài")
            print(f"  • Cập nhật (UPDATE) : {total_updated} bài")
            print("=" * 72)

        except Exception as e:
            db.rollback()
            print("\n[LỖI] Đã rollback giao dịch database:", e)
            raise


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Nâng cấp toàn diện nội dung bài học Toán, Lý, Hóa.")
    parser.add_argument(
        "--subject",
        choices=["all", "math", "physics", "chemistry"],
        default="all",
        help="Chọn môn học cần nâng cấp (mặc định: all)",
    )
    parser.add_argument(
        "--grade",
        type=int,
        default=None,
        help="Chỉ nâng cấp một khối lớp cụ thể (từ 1 đến 12)",
    )
    parser.add_argument(
        "--flat-formulas",
        action="store_true",
        help="Lưu trường formulas dưới dạng mảng chuỗi phẳng list[str] thay vì list[dict] phân nhóm",
    )
    parser.add_argument(
        "--db-url",
        default=None,
        help="Chuỗi kết nối Database đích (ví dụ: URL PostgreSQL trên Neon/Render để nâng cấp trực tiếp DB online)",
    )
    args = parser.parse_args()
    update_lessons(
        subject_filter=args.subject,
        grade_filter=args.grade,
        flat_formulas=args.flat_formulas,
    )