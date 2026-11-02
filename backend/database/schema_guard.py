"""Tự bổ sung các cột mới cho bảng `lessons` nếu CSDL chưa có.

Giúp việc deploy không bị lỗi khi code mới (có cột `requirements`, `quiz`)
chạy trên CSDL cũ chưa được cập nhật. Chỉ chạy 1 lần mỗi tiến trình,
và chỉ ALTER khi thật sự thiếu cột (an toàn, không xoá dữ liệu).
"""
from sqlalchemy import inspect, text

NEW_LESSON_COLUMNS = ("requirements", "quiz")

_checked = False


def ensure_lesson_columns(engine) -> list[str]:
    """Thêm cột còn thiếu, trả về danh sách cột vừa thêm."""
    global _checked
    if _checked:
        return []
    added: list[str] = []
    try:
        existing = {c["name"] for c in inspect(engine).get_columns("lessons")}
    except Exception:
        # Bảng chưa tồn tại (sẽ được create_all tạo đủ cột) -> bỏ qua
        _checked = True
        return added
    col_type = "JSONB" if engine.dialect.name == "postgresql" else "JSON"
    missing = [c for c in NEW_LESSON_COLUMNS if c not in existing]
    if missing:
        with engine.begin() as conn:
            for col in missing:
                if engine.dialect.name == "postgresql":
                    conn.execute(text(f"ALTER TABLE lessons ADD COLUMN IF NOT EXISTS {col} {col_type}"))
                else:
                    conn.execute(text(f"ALTER TABLE lessons ADD COLUMN {col} {col_type}"))
                added.append(col)
    _checked = True
    return added
