"""
Tạo lại các bài học Toán (lớp 1-12) trực tiếp trên database trong DATABASE_URL (Neon/SQLite).

Sử dụng bộ dữ liệu 3 cấp chuẩn SGK Kết nối tri thức với cuộc sống từ `math_sgk/lop1.py` .. `lop12.py`
thông qua `import_math_sgk.py`.

Chạy từ thư mục backend:
    python tools/rebuild_math_lessons.py
    python tools/rebuild_math_lessons.py --grades 1-12 --dry-run
"""
import subprocess
import sys
from pathlib import Path

TOOLS_DIR = Path(__file__).resolve().parent


def main():
    cmd = [sys.executable, str(TOOLS_DIR / "import_math_sgk.py"), "--grades", "1-12", *sys.argv[1:]]
    raise SystemExit(subprocess.call(cmd))


if __name__ == "__main__":
    main()
