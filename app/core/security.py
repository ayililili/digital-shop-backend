# app/core/security.py - JWT 簽發模組

import jwt
from datetime import datetime, timedelta, timezone
from app.schemas.user import UserSchema
from app.core.config import settings


def create_jwt_token(user: UserSchema) -> str:
    """
    根據使用者資訊簽發 access token（預設 15 分鐘有效）。
    """
    payload = {
        "sub": user.id,
        "email": user.email,
        "name": user.name,
        "type": "access",
        "exp": datetime.now(timezone.utc)
        + timedelta(minutes=settings.JWT_ACCESS_EXP_MINUTES),
    }

    return jwt.encode(payload, settings.JWT_SECRET, algorithm="HS256")


def create_refresh_token(user: UserSchema) -> str:
    """
    根據使用者資訊簽發 refresh token（預設 7 天有效）。
    """
    payload = {
        "sub": user.id,
        "type": "refresh",
        "exp": datetime.now(timezone.utc)
        + timedelta(days=settings.JWT_REFRESH_EXP_DAYS),
    }

    return jwt.encode(payload, settings.JWT_SECRET, algorithm="HS256")
