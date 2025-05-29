# app/schemas/response.py - 統一 API 回應格式定義

from pydantic import BaseModel
from typing import Generic, TypeVar

# 通用型別 T，提供泛型支援
T = TypeVar("T")


class SuccessResponse(BaseModel, Generic[T]):
    """
    {
        "status": "success",
        "data": { ... }
    }
    """

    status: str = "success"
    data: T


class ErrorObject(BaseModel):
    code: int
    message: str
    type: str


class ErrorResponse(BaseModel):
    """
    {
        "status": "error",
        "error": {
            "code": 401,
            "message": "Unauthorized",
            "type": "AuthError"
        }
    }
    """

    status: str = "error"
    error: ErrorObject
