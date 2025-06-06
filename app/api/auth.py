# app/api/auth.py - 登入 API 路由

from fastapi import APIRouter, Cookie
from fastapi.responses import JSONResponse
import jwt
from app.core.config import settings
from app.core.errors import AuthError, BadRequestError, NotFoundError
from app.schemas.auth import LoginRequest, LoginResponse
from app.schemas.response import SuccessResponse
from app.core.security import create_jwt_token, create_refresh_token
from app.services.firebase_auth import verify_id_token
from app.services.firestore.user import get_or_create_user, get_user
from app.schemas.user import UserSchema

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/google-login", response_model=SuccessResponse[LoginResponse])
def google_login(data: LoginRequest):
    """
    接收 Google id_token，透過 Firebase 驗證。
    若為新用戶則註冊，否則登入。
    回傳 access token 與使用者資訊，refresh token 設定為 HttpOnly Cookie。
    """
    decoded = verify_id_token(data.id_token)
    user: UserSchema = get_or_create_user(decoded)

    access_token = create_jwt_token(user)
    refresh_token = create_refresh_token(user)

    response = JSONResponse(
        content=SuccessResponse(
            data=LoginResponse(access_token=access_token, user=user)
        ).model_dump(mode="json")
    )

    response.set_cookie(
        key="refresh_token",
        value=refresh_token,
        httponly=True,
        secure=True,  # 僅在 HTTPS 上傳輸
        samesite="strict",
        path="/auth/refresh-token",
        max_age=60 * 60 * 24 * settings.JWT_REFRESH_EXP_DAYS,  # 單位秒
    )

    return response


@router.post("/refresh-token", response_model=SuccessResponse[LoginResponse])
def refresh_token(refresh_token: str = Cookie(None)):
    """
    根據 HttpOnly Cookie 中的 refresh token 取得新 access token。
    """
    if refresh_token is None:
        raise AuthError("缺少 refresh token")

    try:
        payload = jwt.decode(refresh_token, settings.JWT_SECRET, algorithms=["HS256"])

        if payload.get("type") != "refresh":
            raise BadRequestError("無效的 token 類型")

        user_id = payload.get("sub")
        user = get_user(user_id)

        new_access_token = create_jwt_token(user)
        new_refresh_token = create_refresh_token(user)

        response = JSONResponse(
            content=SuccessResponse(
                data=LoginResponse(access_token=new_access_token, user=user)
            ).model_dump(mode="json")
        )

        response.set_cookie(
            key="refresh_token",
            value=new_refresh_token,
            httponly=True,
            secure=True,  # 僅在 HTTPS 上傳輸
            samesite="strict",
            path="/auth/refresh-token",
            max_age=60 * 60 * 24 * settings.JWT_REFRESH_EXP_DAYS,  # 單位秒
        )

        return response

    except jwt.ExpiredSignatureError:
        raise AuthError("Refresh token 已過期")
    except jwt.InvalidTokenError:
        raise AuthError("無效的 refresh token")
    except ValueError:
        raise NotFoundError("使用者不存在")
