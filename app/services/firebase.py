# app/services/firebase.py - Firebase 驗證工具

import firebase_admin
from firebase_admin import credentials, auth
import os
from dotenv import load_dotenv

load_dotenv()

# 初始化 Firebase App（只初始化一次）
if not firebase_admin._apps:
    cred_path = os.getenv("FIREBASE_CREDENTIALS")
    cred = credentials.Certificate(cred_path)
    firebase_admin.initialize_app(cred)


def verify_id_token(id_token: str) -> dict:
    """
    驗證 Google id_token 並回傳解析後的使用者資訊。
    """
    decoded_token = auth.verify_id_token(id_token)
    return decoded_token
