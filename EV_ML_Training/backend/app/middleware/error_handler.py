from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from app.exceptions.custom_exceptions import BaseAPIException
from app.utils.logging_config import logger
from app.schemas.common import ErrorResponse
import json

async def custom_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    request_id = getattr(request.state, "request_id", None)
    
    if isinstance(exc, BaseAPIException):
        error_resp = ErrorResponse(
            error_code=exc.error_code,
            message=exc.message,
            details=exc.details,
            request_id=request_id
        )
        logger.error(f"API Exception (req_id: {request_id}): {exc.message} | Details: {exc.details}")
        return JSONResponse(status_code=exc.status_code, content=error_resp.model_dump())
        
    if isinstance(exc, RequestValidationError):
        details = {"validation_errors": exc.errors()}
        error_resp = ErrorResponse(
            error_code="VALIDATION_ERROR",
            message="Request validation failed.",
            details=details,
            request_id=request_id
        )
        logger.error(f"Validation Error (req_id: {request_id}): {details}")
        return JSONResponse(status_code=422, content=error_resp.model_dump())
        
    if isinstance(exc, json.JSONDecodeError):
        error_resp = ErrorResponse(
            error_code="MALFORMED_JSON",
            message="Malformed JSON in request body.",
            request_id=request_id
        )
        logger.error(f"Malformed JSON (req_id: {request_id}): {str(exc)}")
        return JSONResponse(status_code=400, content=error_resp.model_dump())

    # Catch-all
    error_resp = ErrorResponse(
        error_code="INTERNAL_SERVER_ERROR",
        message="An unexpected internal error occurred.",
        request_id=request_id
    )
    logger.exception(f"Unexpected Error (req_id: {request_id}): {str(exc)}")
    return JSONResponse(status_code=500, content=error_resp.model_dump())

def register_exception_handlers(app):
    @app.exception_handler(BaseAPIException)
    async def base_api_exception_handler(request: Request, exc: BaseAPIException):
        return await custom_exception_handler(request, exc)

    @app.exception_handler(Exception)
    async def global_exception_handler(request: Request, exc: Exception):
        return await custom_exception_handler(request, exc)
