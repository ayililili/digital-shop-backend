# app/services/firestore/user.py - Firestore 使用者操作模組

import uuid
from datetime import datetime, timezone
from typing import Dict

from app.core.firestore_client import get_firestore_client
from app.schemas.user import UserSchema


def get_or_create_user_by_firebase_uid(decoded: Dict) -> UserSchema:
    """
    根據 Firebase 驗證結果中的 UID 查詢或創建使用者。
    """
    db = get_firestore_client()
    users_collection = db.collection("users")

    firebase_uid = decoded["uid"]
    doc_ref = users_collection.document(firebase_uid)
    doc = doc_ref.get()

    if doc.exists:
        user_data = doc.to_dict()
    else:
        user_data = {
            "id": str(uuid.uuid4()),
            "firebase_uid": firebase_uid,
            "email": decoded.get("email", ""),
            "name": decoded.get("name", ""),
            "picture": decoded.get("picture", ""),
            "created_at": datetime.now(timezone.utc),
        }
        doc_ref.set(user_data)

    return UserSchema(**user_data)
