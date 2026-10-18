import os
from pathlib import Path

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

connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}

engine_kwargs = {"connect_args": connect_args, "pool_pre_ping": True}
if IS_VERCEL:
    # Serverless: mỗi lần gọi là một instance ngắn hạn, không giữ pool kết nối
    engine_kwargs["poolclass"] = NullPool

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
