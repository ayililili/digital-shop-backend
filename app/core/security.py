# app/core/security.py - JWT 簽發模組

import jwt
from datetime import datetime, timedelta, timezone
from app.schemas.user import UserSchema
from app.core.config import settings


def create_jwt_token(user: UserSchema) -> str:
    """
    根據使用者資訊簽發 JWT，預設有效時間 60 分鐘。
    僅接受 UserSchema 類型。
    """

    payload = {
        "sub": user.id,
        "email": user.email,
        "name": user.name,
        "exp": datetime.now(timezone.utc) + timedelta(minutes=settings.JWT_EXP_MINUTES),
    }

    return jwt.encode(payload, settings.JWT_SECRET, algorithm="HS256")
