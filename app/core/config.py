# app/core/config.py - 專案設定集中管理

import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    JWT_SECRET: str = os.getenv("JWT_SECRET", "")
    JWT_ACCESS_EXP_MINUTES: int = 15
    JWT_REFRESH_EXP_DAYS: int = 7
    FIREBASE_CREDENTIALS: str = os.getenv("FIREBASE_CREDENTIALS", "")
    # 允許跨域的前端來源，逗號分隔
    CORS_ORIGINS: list[str] = [origin.strip() for origin in os.getenv("CORS_ORIGINS", "http://localhost:5173").split(",")]


settings = Settings()
