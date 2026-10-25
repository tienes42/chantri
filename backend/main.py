import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware

from database.database import Base, engine
from models import *  # noqa: F401,F403
from routers import content, games, health

# Tự tạo bảng khi chạy local. Trên Vercel bỏ qua (tạo bảng 1 lần bằng backend/tools/init_db.py).
if not os.getenv("VERCEL"):
    Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="HỌC ĐỂ LÀM GÌ API",
    version="0.2.1",
    description="Backend cho nền tảng học tập tương tác HỌC ĐỂ LÀM GÌ.",
)

# Nén GZip tự động cho các phản hồi JSON lớn (danh sách bài học)
app.add_middleware(GZipMiddleware, minimum_size=500)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router, prefix="/api")
app.include_router(content.router, prefix="/api")
app.include_router(games.router, prefix="/api")

@app.get("/")
def root():
    return {
        "name": "HỌC ĐỂ LÀM GÌ",
        "status": "running",
        "version": app.version,
        "docs": "/docs",
    }
