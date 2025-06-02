# app/services/firebase_auth.py - Firebase 驗證封裝

from firebase_admin import auth, exceptions as firebase_exceptions
from app.core.firebase_app import get_firebase_app
from app.core.errors import AuthError
from app.schemas.auth import FirebaseDecodedToken


def verify_id_token(id_token: str) -> FirebaseDecodedToken:
    """
    驗證 Google id_token 並回傳解析後的使用者資訊。
    發生錯誤時統一轉為 AuthError。
    """
    try:
        # 確保 Firebase App 已初始化（只會執行一次）
        get_firebase_app()
        decoded_raw = auth.verify_id_token(id_token)
        return FirebaseDecodedToken(**decoded_raw)
    except firebase_exceptions.FirebaseError:
        raise AuthError("ID token 驗證失敗，請重新登入")
