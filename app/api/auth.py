# app/api/auth.py - 登入 API 路由

from fastapi import APIRouter
from app.schemas.auth import LoginRequest, LoginResponse
from app.schemas.response import SuccessResponse
from app.core.security import create_jwt_token, create_refresh_token
from app.services.firebase_auth import verify_id_token
from app.services.firestore.user import get_or_create_user_by_firebase_uid
from app.schemas.user import UserResponse

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/google-login", response_model=SuccessResponse[LoginResponse])
def google_login(data: LoginRequest):
    """
    接收 Google id_token，透過 Firebase 驗證。
    若為新用戶則註冊，否則登入。
    回傳 access token、refresh token 與使用者資訊。
    """
    decoded = verify_id_token(data.id_token)
    user: UserResponse = get_or_create_user_by_firebase_uid(decoded)

    access_token = create_jwt_token(user)
    refresh_token = create_refresh_token(user)

    return SuccessResponse(
        data=LoginResponse(
            access_token=access_token, refresh_token=refresh_token, user=user
        )
    )
