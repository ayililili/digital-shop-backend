# app/core/firestore_client.py - Firestore 初始化模組

from google.cloud import firestore
from google.oauth2 import service_account
from app.core.config import settings

# 取得憑證檔案路徑
cred_path = settings.FIREBASE_CREDENTIALS
if not cred_path:
    raise RuntimeError("FIREBASE_CREDENTIALS 環境變數未設定")

# 初始化 Firestore 客戶端（僅初始化一次）
credentials = service_account.Credentials.from_service_account_file(cred_path)
db = firestore.Client(credentials=credentials)
