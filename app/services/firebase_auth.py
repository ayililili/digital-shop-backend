# app/services/firebase_auth.py - Firebase 驗證封裝

from firebase_admin import auth, exceptions as firebase_exceptions
from app.core.firebase_app import firebase_app
from app.core.errors import AuthError


def verify_id_token(id_token: str) -> dict:
    """
    驗證 Google id_token 並回傳解析後的使用者資訊。
    發生錯誤時統一轉為 AuthError。
    """
    try:
        return auth.verify_id_token(id_token)
    except firebase_exceptions.FirebaseError:
        raise AuthError("ID token 驗證失敗，請重新登入")
