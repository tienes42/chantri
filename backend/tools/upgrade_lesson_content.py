import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
"""
Master Upgrade Script – Đồng bộ & Nâng cấp toàn bộ nội dung bài học các môn (Toán, Vật lý, Hóa học).

Toàn bộ dữ liệu chi tiết từ `upgrade_lesson_content.py` cũ đã được hợp nhất và mở rộng hoàn chỉnh vào:
  1. `upgrade_math_1_9.py`   : 54 bài Toán Lớp 1–9 (6 bài/lớp)
  2. `upgrade_math_10_12.py` : 24 bài Toán Lớp 10–12 (8 bài/lớp)
  3. `upgrade_physics.py`    : 50 bài Vật lý Lớp 6–12 (7–8 bài/lớp)
  4. `upgrade_chemistry.py`  : 49 bài Hóa học Lớp 6–12 (7 bài/lớp)
  => Tổng cộng: 177 bài học chuẩn GDPT 2018.

Cách chạy từ thư mục backend:
  - Nâng cấp TẤT CẢ các môn và các lớp:
        python upgrade_lesson_content.py
  - Chỉ nâng cấp 1 môn cụ thể (math / physics / chemistry):
        python upgrade_lesson_content.py --subject math
  - Chỉ nâng cấp 1 lớp cụ thể:
        python upgrade_lesson_content.py --grade 12
"""

from sqlalchemy import select
from database.database import SessionLocal
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


def upsert_subject_lessons(db, subject_slug, lessons_data, grade_filter=None):
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
            if hasattr(lesson, key):
                setattr(lesson, key, value)

        print(f"  [{status}] {subject_slug.upper()} | Lớp {item['grade']:>2} | {item['topic']:<32} | {item['title']}")

    return created, updated


def update_lessons(subject_filter="all", grade_filter=None):
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

                c, u = upsert_subject_lessons(db, slug, lessons_list, grade_filter=grade_filter)
                total_created += c
                total_updated += u

            db.commit()

            print("\n" + "=" * 72)
            print("HOÀN TẤT NÂNG CẤP TOÀN BỘ DỮ LIỆU BÀI HỌC BACKEND")
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
    args = parser.parse_args()
    update_lessons(subject_filter=args.subject, grade_filter=args.grade)