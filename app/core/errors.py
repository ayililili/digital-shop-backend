# app/core/errors.py - 自定義錯誤類別


class AppBaseError(Exception):
    def __init__(
        self, message: str, status_code: int = 400, error_type: str = "AppError"
    ):
        self.message = message
        self.status_code = status_code
        self.type = error_type


class AuthError(AppBaseError):
    def __init__(self, message: str = "Unauthorized"):
        super().__init__(message, status_code=401, error_type="AuthError")


class NotFoundError(AppBaseError):
    def __init__(self, message: str = "Resource not found"):
        super().__init__(message, status_code=404, error_type="NotFoundError")


class BadRequestError(AppBaseError):
    def __init__(self, message: str = "Bad request"):
        super().__init__(message, status_code=400, error_type="BadRequestError")
