# app/main.py - FastAPI 應用主進入點

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import auth
from app.core.config import settings
from app.core.exception import register_exception_handlers

# 初始化 FastAPI 應用
app = FastAPI()

# 設定 CORS，允許前端呼叫 API
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 掛載 API 路由
app.include_router(auth.router)

# 註冊全域例外處理器
register_exception_handlers(app)


@app.get("/")
def root():
    """
    健康檢查根路由，用於確認 API 是否啟動成功。
    """
    return {"message": "Hello from FastAPI + Poetry on Windows"}
