# app/main.py - FastAPI 應用主進入點

from fastapi import FastAPI

# 初始化 FastAPI 應用
app = FastAPI()


@app.get("/")
def root():
    """
    健康檢查根路由，用於確認 API 是否啟動成功。
    """
    return {"message": "Hello from FastAPI + Poetry on Windows 🎉"}
