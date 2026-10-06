from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request
import uuid
import time
from app.utils.logging_config import logger

class RequestLoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Request ID handling
        request_id = request.headers.get("X-Request-ID")
        if not request_id or len(request_id) > 50: # safe length
            request_id = str(uuid.uuid4())
            
        request.state.request_id = request_id
        
        start_time = time.time()
        
        logger.info(f"Request started: {request.method} {request.url.path} (req_id: {request_id})")
        
        try:
            response = await call_next(request)
            process_time = time.time() - start_time
            logger.info(f"Request completed: {request.method} {request.url.path} | Status: {response.status_code} | Duration: {process_time:.4f}s (req_id: {request_id})")
            
            response.headers["X-Request-ID"] = request_id
            return response
        except Exception as e:
            process_time = time.time() - start_time
            logger.error(f"Request failed: {request.method} {request.url.path} | Error: {str(e)} | Duration: {process_time:.4f}s (req_id: {request_id})")
            raise e
