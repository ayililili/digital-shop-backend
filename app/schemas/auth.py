# app/schemas/auth.py - 認證相關資料模型

from pydantic import BaseModel
from app.schemas.user import UserResponse


class LoginRequest(BaseModel):
    id_token: str


class LoginResponse(BaseModel):
    access_token: str
    refresh_token: str
    user: UserResponse
