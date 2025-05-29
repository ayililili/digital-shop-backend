# app/core/exception.py - 全域異常處理器

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.schemas.response import ErrorResponse, ErrorObject
from app.core.errors import AppBaseError


def register_exception_handlers(app: FastAPI):
    @app.exception_handler(AppBaseError)
    async def app_error_handler(request: Request, exc: AppBaseError):
        return JSONResponse(
            status_code=exc.status_code,
            content=ErrorResponse(
                status="error",
                error=ErrorObject(
                    code=exc.status_code, message=exc.message, type=exc.type
                ),
            ).model_dump(),
        )

    @app.exception_handler(Exception)
    async def fallback_handler(request: Request, exc: Exception):
        return JSONResponse(
            status_code=500,
            content=ErrorResponse(
                status="error",
                error=ErrorObject(
                    code=500, message="Internal Server Error", type="ServerError"
                ),
            ).model_dump(),
        )
