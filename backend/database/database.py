import os
from pathlib import Path
from sqlalchemy.dialects.sqlite.base import SQLiteTypeCompiler
if not hasattr(SQLiteTypeCompiler, "visit_JSONB"):
    SQLiteTypeCompiler.visit_JSONB = SQLiteTypeCompiler.visit_JSON

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy.pool import NullPool


# Đọc backend/.env khi chạy local (trên Vercel dùng Environment Variables)
BASE_DIR = Path(__file__).resolve().parents[1]
load_dotenv(BASE_DIR / ".env")

IS_VERCEL = bool(os.getenv("VERCEL"))


def _normalize_url(url: str) -> str:
    """Chấp nhận URL kiểu postgres:// hoặc postgresql:// (Neon, Supabase, Vercel Postgres...)
    và đổi sang driver psycopg v3 mà project đang dùng."""
    url = url.strip()
    if url.startswith("postgres://"):
        url = "postgresql://" + url[len("postgres://"):]
    if url.startswith("postgresql://"):
        url = "postgresql+psycopg://" + url[len("postgresql://"):]
    return url


DATABASE_URL = _normalize_url(
    os.getenv("DATABASE_URL")
    or os.getenv("POSTGRES_URL")
    or "sqlite:///./hoc_de_lam_gi_dev.db"
)

if IS_VERCEL and DATABASE_URL.startswith("sqlite"):
    raise RuntimeError(
        "Thiếu biến môi trường DATABASE_URL trên Vercel. "
        "Vào Project Settings > Environment Variables và thêm chuỗi kết nối PostgreSQL."
    )

if DATABASE_URL.startswith("sqlite"):
    connect_args = {"check_same_thread": False}
    engine_kwargs = {"connect_args": connect_args, "pool_pre_ping": True}
else:
    connect_args = {"connect_timeout": 10, "prepare_threshold": None}
    engine_kwargs = {"connect_args": connect_args, "pool_pre_ping": True}
    if IS_VERCEL:
        # Serverless + Neon Pooler: đóng kết nối gọn sau mỗi lần thực thi, tương thích hoàn toàn với PgBouncer (-pooler)
        engine_kwargs["poolclass"] = NullPool
    else:
        engine_kwargs["pool_size"] = 5
        engine_kwargs["max_overflow"] = 10

engine = create_engine(DATABASE_URL, **engine_kwargs)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


class Base(DeclarativeBase):
    pass


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
