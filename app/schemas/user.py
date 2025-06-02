# app/schemas/user.py - 使用者資料模型

from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class UserSchema(BaseModel):
    id: str  # Firebase UID
    email: str
    name: Optional[str]
    picture: Optional[str]
    created_at: datetime
    last_login: datetime
