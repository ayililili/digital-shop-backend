# app/core/firestore_client.py - Firestore 初始化模組

from google.cloud import firestore
from google.oauth2 import service_account
from app.core.config import settings
from app.core.errors import FirebaseCredentialFileNotFound, FirebaseCredentialNotSet

_db = None  # 單例實例


def get_firestore_client():
    """
    初始化 Firestore Client（若尚未初始化），並回傳實例。
    """
    global _db

    if _db:
        return _db

    if not settings.FIREBASE_CREDENTIALS:
        raise FirebaseCredentialNotSet()

    try:
        credentials = service_account.Credentials.from_service_account_file(
            settings.FIREBASE_CREDENTIALS
        )
    except FileNotFoundError:
        raise FirebaseCredentialFileNotFound(settings.FIREBASE_CREDENTIALS)

    _db = firestore.Client(credentials=credentials)
    return _db
