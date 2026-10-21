import os
import sys
from pathlib import Path

# Đảm bảo luôn tìm thấy thư mục gốc `backend/` và nạp đúng file `backend/.env`
# dù chạy lệnh từ `backend/` hay `backend/tools/`
BACKEND_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BACKEND_DIR))

try:
    from dotenv import load_dotenv
    env_path = BACKEND_DIR / ".env"
    if env_path.exists():
        load_dotenv(dotenv_path=env_path, override=True)
except ImportError:
    pass

# Hỗ trợ tương thích tự động kiểu JSONB của PostgreSQL khi chạy trên SQLite
from sqlalchemy.dialects.sqlite.base import SQLiteTypeCompiler
if not hasattr(SQLiteTypeCompiler, "visit_JSONB"):
    SQLiteTypeCompiler.visit_JSONB = SQLiteTypeCompiler.visit_JSON

"""
Khởi tạo các bảng cơ sở dữ liệu (SQLAlchemy) và tự động seed 3 môn học mặc định (Toán, Vật lý, Hóa học).

Chạy từ thư mục backend hoặc backend/tools:
    python init_db.py
"""

from sqlalchemy import select
from database.database import Base, SessionLocal, engine

# Import tất cả models để SQLAlchemy đăng ký đầy đủ các bảng
from models.user import User
from models.subject import Subject
from models.lesson import Lesson
from models.game import Game
from models.progress import Progress
from models.game_session import GameSession
from models.game_event import GameEvent

DEFAULT_SUBJECTS = [
    {"slug": "math", "name": "Toán"},
    {"slug": "physics", "name": "Vật lý"},
    {"slug": "chemistry", "name": "Hóa học"},
]


def init_db():
    print(f"[INFO] Đang kết nối Database: {engine.url.render_as_string(hide_password=True)}")
    Base.metadata.create_all(bind=engine)
    print("[OK] Đã tạo/kiểm tra toàn bộ các bảng trong cơ sở dữ liệu.")

    with SessionLocal() as db:
        try:
            for item in DEFAULT_SUBJECTS:
                subject = db.scalar(select(Subject).where(Subject.slug == item["slug"]))
                if subject is None:
                    subject = Subject(slug=item["slug"], name=item["name"])
                    db.add(subject)
                    db.flush()
                    print(f"  + Đã khởi tạo môn học: {item['name']} (slug='{item['slug']}', id={subject.id})")
                else:
                    print(f"  • Đã có môn học: {subject.name} (slug='{subject.slug}', id={subject.id})")
            db.commit()
        except Exception:
            db.rollback()
            raise


if __name__ == "__main__":
    init_db()