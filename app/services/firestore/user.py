# app/services/firestore/user.py - Firestore 使用者操作模組

from datetime import datetime, timezone
from app.core.firestore_client import get_firestore_client
from app.schemas.user import UserSchema
from app.schemas.auth import FirebaseDecodedToken
from app.core.errors import NotFoundError


def get_user(uid: str) -> UserSchema:
    """
    根據 UID 取得使用者資料。
    若不存在則拋出 NotFoundError。
    """
    db = get_firestore_client()
    users_collection = db.collection("users")
    doc_ref = users_collection.document(uid)
    doc = doc_ref.get()

    if not doc.exists:
        raise NotFoundError(f"使用者 {uid} 不存在")

    user_data = doc.to_dict()
    user_data["id"] = uid
    return UserSchema(**user_data)


def get_or_create_user(decoded: FirebaseDecodedToken) -> UserSchema:
    """
    根據 Firebase 解碼的使用者資訊取得或建立使用者。
    若使用者存在則更新 last_login，否則建立新使用者。
    """
    db = get_firestore_client()
    users_collection = db.collection("users")

    uid = decoded.uid
    doc_ref = users_collection.document(uid)
    doc = doc_ref.get()

    now = datetime.now(timezone.utc)

    if doc.exists:
        user_data = doc.to_dict()
        user_data["id"] = uid
        user_data["last_login"] = now
        doc_ref.update({"last_login": now})
    else:
        user_data = {
            "id": uid,
            "email": decoded.email or "",
            "name": decoded.name or "",
            "picture": decoded.picture or "",
            "created_at": now,
            "last_login": now,
        }
        doc_ref.set(user_data)

    return UserSchema(**user_data)
