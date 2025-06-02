# app/schemas/user.py - 使用者資料模型

from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class UserInDB(BaseModel):
    """
    Firestore 使用者實際儲存結構。
    """

    id: str  # internal UUID
    firebase_uid: str
    email: str
    name: Optional[str] = None
    picture: Optional[str] = None
    created_at: datetime
    last_login: datetime


class UserResponse(BaseModel):
    """
    回傳給前端使用的使用者資訊，不包含敏感欄位。
    """

    id: str
    email: str
    name: Optional[str] = None
    picture: Optional[str] = None
    created_at: datetime
    last_login: datetime
