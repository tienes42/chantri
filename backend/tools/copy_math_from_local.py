"""
Đồng bộ toàn bộ bài học các môn (Toán, Vật lý, Hóa học) từ database LOCAL (Docker) sang database ONLINE (Neon).

Chạy từ thư mục backend:
    docker start hoc-de-lam-gi-postgres
    python copy_math_from_local.py
    (Hoặc chỉ đồng bộ 1 môn: python copy_math_from_local.py --subject math)
    (Hoặc chỉ thêm bài mới mà không ghi đè: python copy_math_from_local.py --no-overwrite)

Điểm nâng cấp so với phiên bản cũ:
1. Hỗ trợ đồng bộ cả 3 môn: Toán (math), Vật lý (physics), Hóa học (chemistry) thay vì chỉ riêng môn Toán.
2. Chế độ Upsert mặc định: Vừa thêm bài học mới chưa có trên Neon, vừa cập nhật nội dung chi tiết & công thức mới cho các bài đã có (giữ nguyên ID bài học trên Neon để không làm mất tiến độ học tập của người dùng).
"""
import argparse
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker

from database.database import SessionLocal as OnlineSession, DATABASE_URL
from models.lesson import Lesson
from models.subject import Subject

LOCAL_URL = os.getenv(
    "LOCAL_DATABASE_URL",
    "postgresql+psycopg://hoc_user:change_me@localhost:5432/hoc_de_lam_gi",
)


def sync_local_to_online(subject_filter="all", overwrite=True):
    if "localhost" in DATABASE_URL or "127.0.0.1" in DATABASE_URL or DATABASE_URL.startswith("sqlite"):
        sys.exit(
            "[CẢNH BÁO] DATABASE_URL trong backend/.env đang trỏ về máy local.\n"
            "Hãy dán chuỗi kết nối Neon (online) vào DATABASE_URL trước khi chạy đồng bộ."
        )

    local = sessionmaker(bind=create_engine(LOCAL_URL))()
    online = OnlineSession()

    columns = [c.name for c in Lesson.__table__.columns if c.name not in ("id", "subject_id")]

    try:
        query = select(Subject)
        if subject_filter != "all":
            query = query.where(Subject.slug == subject_filter)

        local_subjects = local.scalars(query).all()
        if not local_subjects:
            sys.exit(f"Không tìm thấy môn học nào trong database local (filter={subject_filter}).")

        total_added = 0
        total_updated = 0
        total_skipped = 0

        for l_subject in local_subjects:
            o_subject = online.scalar(select(Subject).where(Subject.slug == l_subject.slug))
            if o_subject is None:
                o_subject = Subject(slug=l_subject.slug, name=l_subject.name)
                online.add(o_subject)
                online.flush()
                print(f"[CREATE SUBJECT] Đã tạo môn '{l_subject.name}' ({l_subject.slug}) trên Neon.")

            local_lessons = local.scalars(
                select(Lesson)
                .where(Lesson.subject_id == l_subject.id)
                .order_by(Lesson.grade, Lesson.id)
            ).all()

            online_lessons_map = {
                (l.grade, l.topic): l
                for l in online.scalars(select(Lesson).where(Lesson.subject_id == o_subject.id)).all()
            }

            added = 0
            updated = 0
            skipped = 0

            for l in local_lessons:
                key = (l.grade, l.topic)
                if key not in online_lessons_map:
                    online.add(Lesson(subject_id=o_subject.id, **{c: getattr(l, c) for c in columns}))
                    added += 1
                elif overwrite:
                    o_lesson = online_lessons_map[key]
                    for c in columns:
                        setattr(o_lesson, c, getattr(l, c))
                    updated += 1
                else:
                    skipped += 1

            print(
                f"[{l_subject.slug.upper()}] Local có {len(local_lessons)} bài -> "
                f"Thêm mới: {added}, Cập nhật: {updated}, Bỏ qua: {skipped}"
            )
            total_added += added
            total_updated += updated
            total_skipped += skipped

        online.commit()
        print("\n" + "=" * 60)
        print("ĐỒNG BỘ LOCAL -> NEON THÀNH CÔNG!")
        print(f"  • Thêm mới : {total_added} bài")
        print(f"  • Cập nhật : {total_updated} bài")
        print(f"  • Bỏ qua   : {total_skipped} bài")
        print("=" * 60)

    except Exception:
        online.rollback()
        raise
    finally:
        local.close()
        online.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Đồng bộ bài học từ Local Docker sang Online Neon.")
    parser.add_argument(
        "--subject",
        default="all",
        help="Slug môn học cần đồng bộ (math, physics, chemistry hoặc all)",
    )
    parser.add_argument(
        "--no-overwrite",
        action="store_true",
        help="Chỉ thêm bài chưa có, không cập nhật bài đã tồn tại trên Neon",
    )
    args = parser.parse_args()
    sync_local_to_online(subject_filter=args.subject, overwrite=not args.no_overwrite)