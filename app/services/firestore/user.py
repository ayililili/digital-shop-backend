# app/services/firestore/user.py - Firestore 使用者操作模組

import uuid
from datetime import datetime, timezone
from typing import Dict

from app.core.firestore_client import get_firestore_client
from app.schemas.user import UserResponse


def get_or_create_user_by_firebase_uid(decoded: Dict) -> UserResponse:
    """
    根據 Firebase UID 獲取或創建使用者資料。
    如果使用者已存在，則更新最後登入時間；如果不存在，則創建新使用者。
    使用 internal UUID 作為 user.id，Firebase UID 作為外部綁定識別。
    """
    db = get_firestore_client()
    users_collection = db.collection("users")

    firebase_uid = decoded["uid"]
    doc_ref = users_collection.document(firebase_uid)
    doc = doc_ref.get()

    now = datetime.now(timezone.utc)

    if doc.exists:
        user_data = doc.to_dict()
        user_data["last_login"] = now
        doc_ref.update({"last_login": now})
    else:
        user_data = {
            "id": str(uuid.uuid4()),  # internal UUID
            "firebase_uid": firebase_uid,
            "email": decoded.get("email", ""),
            "name": decoded.get("name", ""),
            "picture": decoded.get("picture", ""),
            "created_at": now,
            "last_login": now,
        }
        doc_ref.set(user_data)

    return UserResponse(**user_data)
