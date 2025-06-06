# app/core/config.py - 專案設定集中管理

import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    # ========== 環境模式 ==========
    APP_ENV: str = os.getenv("APP_ENV", "production").lower()

    @property
    def is_dev(self) -> bool:
        return self.APP_ENV == "development"

    @property
    def is_prod(self) -> bool:
        return self.APP_ENV == "production"

    # ========== JWT ==========
    JWT_SECRET: str = os.getenv("JWT_SECRET", "")
    JWT_ACCESS_EXP_MINUTES: int = 15
    JWT_REFRESH_EXP_DAYS: int = 7

    # ========== Firebase ==========
    FIREBASE_CREDENTIALS: str = os.getenv("FIREBASE_CREDENTIALS", "")

    # ========== Google Cloud Storage ==========
    GCS_BUCKET_NAME: str = os.getenv("GCS_BUCKET_NAME", "")

    # ========== Stripe ==========
    STRIPE_SECRET_KEY: str = os.getenv("STRIPE_SECRET_KEY", "")
    STRIPE_WEBHOOK_SECRET: str = os.getenv("STRIPE_WEBHOOK_SECRET", "")

    # ========== CORS ==========
    CORS_ORIGINS: list[str] = [
        origin.strip()
        for origin in os.getenv("CORS_ORIGINS", "http://localhost:5173").split(",")
    ]


settings = Settings()
