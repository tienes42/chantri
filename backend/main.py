import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database.database import Base, engine
from models import *  # noqa: F401,F403
from routers import content, games, health

# Tự tạo bảng khi chạy local. Trên Vercel bỏ qua (tạo bảng 1 lần bằng backend/tools/init_db.py).
if not os.getenv("VERCEL"):
    Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="HỌC ĐỂ LÀM GÌ API",
    version="0.2.0",
    description="Backend cho nền tảng học tập tương tác HỌC ĐỂ LÀM GÌ.",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500",
        "http://127.0.0.1:3000",
        "http://localhost:3000",
    ],
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
