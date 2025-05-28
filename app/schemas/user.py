# app/schemas/user.py - 使用者資料模型

from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class UserSchema(BaseModel):
    id: str
    firebase_uid: str
    email: str
    name: Optional[str] = None
    picture: Optional[str] = None
    created_at: datetime
