# app/api/auth.py - 登入 API 路由

from fastapi import APIRouter
from app.schemas.auth import LoginRequest, LoginResponse
from app.schemas.response import SuccessResponse
from app.core.security import create_jwt_token
from app.services.firebase_auth import verify_id_token
from app.services.firestore.user import get_or_create_user_by_firebase_uid
from app.schemas.user import UserSchema

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/google-login", response_model=SuccessResponse[LoginResponse])
def google_login(data: LoginRequest):
    """
    接收 Google id_token，透過 Firebase 驗證。
    若為新用戶則註冊，否則登入。
    回傳自簽 JWT 與使用者資訊。
    """
    decoded = verify_id_token(data.id_token)
    user: UserSchema = get_or_create_user_by_firebase_uid(decoded)
    token = create_jwt_token(user)

    return SuccessResponse(data=LoginResponse(token=token, user=user))
