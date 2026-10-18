"""
Copy các bài học Toán từ database LOCAL (Docker) sang database ONLINE (Neon).

Chạy từ thư mục backend:
    docker start hoc-de-lam-gi-postgres
    python tools\\copy_math_from_local.py

- Database ONLINE lấy từ DATABASE_URL trong backend\\.env  (Neon)
- Database LOCAL mặc định: postgresql+psycopg://hoc_user:change_me@localhost:5432/hoc_de_lam_gi
  (đổi bằng biến LOCAL_DATABASE_URL nếu khác)
Chỉ thêm bài chưa có (so theo môn + lớp + topic), không xóa hay ghi đè gì.
"""
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

if "localhost" in DATABASE_URL or "127.0.0.1" in DATABASE_URL or DATABASE_URL.startswith("sqlite"):
    sys.exit("DATABASE_URL trong backend\\.env đang trỏ về máy local. Hãy dán chuỗi kết nối Neon vào đó.")

local = sessionmaker(bind=create_engine(LOCAL_URL))()
online = OnlineSession()

columns = [c.name for c in Lesson.__table__.columns if c.name not in ("id", "subject_id")]

try:
    l_subject = local.scalar(select(Subject).where(Subject.slug == "math"))
    if l_subject is None:
        sys.exit("Database local không có môn Toán (slug = math).")

    o_subject = online.scalar(select(Subject).where(Subject.slug == "math"))
    if o_subject is None:
        o_subject = Subject(slug="math", name=l_subject.name)
        online.add(o_subject)
        online.flush()

    local_lessons = local.scalars(select(Lesson).where(Lesson.subject_id == l_subject.id)).all()
    print(f"Local có {len(local_lessons)} bài Toán.")

    existing = {
        (l.grade, l.topic)
        for l in online.scalars(select(Lesson).where(Lesson.subject_id == o_subject.id)).all()
    }

    added = 0
    for l in local_lessons:
        if (l.grade, l.topic) in existing:
            continue
        online.add(Lesson(subject_id=o_subject.id, **{c: getattr(l, c) for c in columns}))
        added += 1

    online.commit()
    print(f"Đã thêm {added} bài Toán lên Neon (bỏ qua {len(local_lessons) - added} bài đã có).")
except Exception:
    online.rollback()
    raise
finally:
    local.close()
    online.close()
