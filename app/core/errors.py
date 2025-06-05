# app/core/errors.py - 自定義錯誤類別


class AppBaseError(Exception):
    def __init__(
        self,
        message: str,
        status_code: int = 400,
        error_type: str = "AppError",
    ):
        self.message = message
        self.status_code = status_code
        self.type = error_type


# ==== 常見錯誤 ====


class AuthError(AppBaseError):
    def __init__(self, message: str = "Unauthorized"):
        super().__init__(message, status_code=401, error_type="AuthError")


class NotFoundError(AppBaseError):
    def __init__(self, message: str = "Resource not found"):
        super().__init__(message, status_code=404, error_type="NotFoundError")


class BadRequestError(AppBaseError):
    def __init__(self, message: str = "Bad request"):
        super().__init__(message, status_code=400, error_type="BadRequestError")


# ==== 設定錯誤（環境變數、初始化） ====


class ConfigError(AppBaseError):
    def __init__(self, message: str = "Invalid configuration"):
        super().__init__(message, status_code=500, error_type="ConfigError")


class FirebaseCredentialNotSet(ConfigError):
    def __init__(self):
        super().__init__(message="FIREBASE_CREDENTIALS 環境變數未設定")


class FirebaseCredentialFileNotFound(ConfigError):
    def __init__(self, path: str):
        super().__init__(message=f"Firebase 憑證檔案不存在: {path}")


class GCSCredentialNotSet(ConfigError):
    def __init__(self):
        super().__init__(message="GCS_CREDENTIALS 環境變數未設定")


class StripeSecretKeyMissing(ConfigError):
    def __init__(self):
        super().__init__(message="STRIPE_SECRET_KEY 環境變數未設定")
