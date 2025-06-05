# app/core/firebase_app.py - 初始化 Firebase App

from firebase_admin import credentials, initialize_app
from app.core.config import settings
from app.core.errors import FirebaseCredentialFileNotFound, FirebaseCredentialNotSet


_app = None  # 單例實例


def get_firebase_app():
    """
    初始化 Firebase App（若尚未初始化），並回傳 app 實例。
    """
    global _app

    if _app:
        return _app

    if not settings.FIREBASE_CREDENTIALS:
        raise FirebaseCredentialNotSet()

    try:
        cred = credentials.Certificate(settings.FIREBASE_CREDENTIALS)
    except FileNotFoundError:
        raise FirebaseCredentialFileNotFound(settings.FIREBASE_CREDENTIALS)

    _app = initialize_app(cred)
    return _app
