"""Wrapper gọi `backend/tools/init_db.py` để tránh trùng lặp mã nguồn."""
import runpy
from pathlib import Path

if __name__ == "__main__":
    runpy.run_path(str(Path(__file__).resolve().parent / "tools" / "init_db.py"), run_name="__main__")