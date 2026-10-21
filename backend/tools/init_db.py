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

# Tương thích tự động kiểu JSONB của PostgreSQL khi chạy trên SQLite
try:
    from sqlalchemy.dialects.sqlite.base import SQLiteTypeCompiler
    if not hasattr(SQLiteTypeCompiler, "visit_JSONB"):
        SQLiteTypeCompiler.visit_JSONB = SQLiteTypeCompiler.visit_JSON
except Exception:
    pass

"""
Khởi tạo các bảng cơ sở dữ liệu (SQLAlchemy), tự động seed 3 môn học mặc định (Toán, Vật lý, Hóa học)
và tự động nạp toàn bộ 177 bài học nếu bảng `lessons` đang trống.

Chạy từ thư mục backend hoặc backend/tools:
    python init_db.py
"""

from sqlalchemy import func, select
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
    print(f"[INFO] Thư mục làm việc hiện tại: {os.getcwd()}")
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

            lesson_count = db.scalar(select(func.count(Lesson.id))) or 0
            print(f"[INFO] Số bài học hiện có trong Database: {lesson_count}")
        except Exception:
            db.rollback()
            raise

    # Nếu bảng lessons đang trống và có sẵn các module bài học thì tự động nạp luôn 177 bài
    if lesson_count == 0:
        try:
            import upgrade_lesson_content
            print("[INFO] Bảng `lessons` đang trống -> Tự động nạp toàn bộ 177 bài học Toán, Lý, Hóa...")
            upgrade_lesson_content.update_lessons(subject_filter="all")
        except ImportError:
            print(
                "[GỢI Ý] Bảng `lessons` đang trống. Hãy chạy tiếp `python upgrade_lesson_content.py` "
                "để nạp đầy đủ bài học."
            )


if __name__ == "__main__":
    init_db()