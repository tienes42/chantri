import sys
from pathlib import Path

# Cho phép import "database", "models", "routers"... nằm trong thư mục backend/
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "backend"))

from main import app  # noqa: E402,F401  (Vercel tự nhận biến `app`)
