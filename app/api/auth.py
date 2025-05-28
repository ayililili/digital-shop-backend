# app/api/auth.py - 登入 API 路由

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from app.services.firebase import verify_id_token
from app.core.jwt import create_jwt_token
from app.schemas.user import UserSchema
from app.services.firestore.user import get_or_create_user_by_firebase_uid

router = APIRouter()


class LoginRequest(BaseModel):
    id_token: str


class LoginResponse(BaseModel):
    token: str
    user: UserSchema


@router.post("/google-login", response_model=LoginResponse)
def google_login(data: LoginRequest):
    """
    接收 Google id_token，透過 Firebase 驗證。
    若為新用戶則註冊，否則登入。
    回傳自簽 JWT 與使用者資訊。
    """
    try:
        decoded = verify_id_token(data.id_token)
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid Google token")

    # Firestore 操作
    user = get_or_create_user_by_firebase_uid(decoded)
    token = create_jwt_token(user)

    return {"token": token, "user": user}
