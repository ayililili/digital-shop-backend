# app/schemas/auth.py - 認證相關資料模型

from pydantic import BaseModel
from app.schemas.user import UserSchema


class LoginRequest(BaseModel):
    id_token: str


class LoginResponse(BaseModel):
    token: str
    user: UserSchema
