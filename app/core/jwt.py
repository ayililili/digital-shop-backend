# app/core/jwt.py - JWT 簽發模組

import jwt
import os
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
from app.schemas.user import UserSchema

load_dotenv()

JWT_SECRET = os.getenv("JWT_SECRET")
JWT_EXP_MINUTES = 60


def create_jwt_token(user: UserSchema) -> str:
    """
    根據使用者資訊簽發 JWT，預設有效時間 60 分鐘。
    僅接受 UserSchema 類型。
    """
    payload = {
        "sub": user.id,
        "email": user.email,
        "name": user.name,
        "exp": datetime.now(timezone.utc) + timedelta(minutes=JWT_EXP_MINUTES),
    }

    if JWT_SECRET is None:
        raise ValueError("JWT_SECRET must be set in .env")

    return jwt.encode(payload, JWT_SECRET, algorithm="HS256")
