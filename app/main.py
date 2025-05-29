# app/main.py - FastAPI 應用主進入點

from fastapi import FastAPI
from app.api import auth
from app.core.exception import register_exception_handlers

# 初始化 FastAPI 應用
app = FastAPI()

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
