# app/core/config.py - 專案設定集中管理

import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    JWT_SECRET: str = os.getenv("JWT_SECRET", "")
    JWT_ACCESS_EXP_MINUTES: int = 60
    JWT_REFRESH_EXP_DAYS: int = 30
    FIREBASE_CREDENTIALS: str = os.getenv("FIREBASE_CREDENTIALS", "")


settings = Settings()
