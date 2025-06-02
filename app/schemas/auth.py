# app/schemas/auth.py - 認證相關資料模型

from typing import Optional
from pydantic import BaseModel
from app.schemas.user import UserSchema


class LoginRequest(BaseModel):
    id_token: str


class LoginResponse(BaseModel):
    access_token: str
    user: UserSchema


class FirebaseDecodedToken(BaseModel):
    uid: str
    email: Optional[str] = None
    name: Optional[str] = None
    picture: Optional[str] = None
