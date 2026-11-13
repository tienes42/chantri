"""Tự bổ sung các cột mới cho bảng `lessons` và `users` nếu CSDL chưa có.

Giúp việc deploy không bị lỗi khi code mới chạy trên CSDL cũ chưa được cập nhật.
Chỉ chạy 1 lần mỗi tiến trình, và chỉ ALTER khi thật sự thiếu cột.
"""
from sqlalchemy import inspect, text

NEW_LESSON_COLUMNS = ("requirements", "quiz")

_checked = False


def ensure_lesson_columns(engine) -> list[str]:
    """Thêm cột còn thiếu cho `lessons` và `users`, trả về danh sách cột vừa thêm."""
    global _checked
    if _checked:
        return []
    added: list[str] = []
    insp = inspect(engine)

    try:
        existing_lessons = {c["name"] for c in insp.get_columns("lessons")}
    except Exception:
        existing_lessons = None

    if existing_lessons is not None:
        col_type = "JSONB" if engine.dialect.name == "postgresql" else "JSON"
        missing = [c for c in NEW_LESSON_COLUMNS if c not in existing_lessons]
        if missing:
            with engine.begin() as conn:
                for col in missing:
                    if engine.dialect.name == "postgresql":
                        conn.execute(text(f"ALTER TABLE lessons ADD COLUMN IF NOT EXISTS {col} {col_type}"))
                    else:
                        conn.execute(text(f"ALTER TABLE lessons ADD COLUMN {col} {col_type}"))
                    added.append(f"lessons.{col}")

    try:
        existing_users = {c["name"] for c in insp.get_columns("users")}
    except Exception:
        existing_users = None

    if existing_users is not None and "firebase_uid" not in existing_users:
        with engine.begin() as conn:
            if engine.dialect.name == "postgresql":
                conn.execute(text("ALTER TABLE users ADD COLUMN IF NOT EXISTS firebase_uid VARCHAR(128)"))
                conn.execute(text("CREATE UNIQUE INDEX IF NOT EXISTS ix_users_firebase_uid ON users (firebase_uid)"))
            else:
                conn.execute(text("ALTER TABLE users ADD COLUMN firebase_uid VARCHAR(128)"))
                conn.execute(text("CREATE UNIQUE INDEX IF NOT EXISTS ix_users_firebase_uid ON users (firebase_uid)"))
            added.append("users.firebase_uid")

    _checked = True
    return added
