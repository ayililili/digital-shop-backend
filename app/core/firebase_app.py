# app/services/firebase_app.py - 初始化 Firebase App

import firebase_admin
from firebase_admin import credentials, initialize_app
from app.core.config import settings


def get_firebase_app():
    """
    初始化 Firebase App（若尚未初始化），並回傳 app 實例。
    """
    if not settings.FIREBASE_CREDENTIALS:
        raise ValueError("FIREBASE_CREDENTIALS is not set in .env")

    if not firebase_admin._apps:
        cred = credentials.Certificate(settings.FIREBASE_CREDENTIALS)
        return initialize_app(cred)
    return firebase_admin.get_app()


# 實際初始化，供其他模組直接 import
firebase_app = get_firebase_app()
