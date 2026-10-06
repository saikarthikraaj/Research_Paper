class BaseAPIException(Exception):
    def __init__(self, message: str, error_code: str, status_code: int = 400, details: dict = None):
        self.message = message
        self.error_code = error_code
        self.status_code = status_code
        self.details = details or {}
        super().__init__(self.message)

class ValidationException(BaseAPIException):
    def __init__(self, message: str, details: dict = None):
        super().__init__(message=message, error_code="VALIDATION_ERROR", status_code=422, details=details)

class MissingFeaturesException(BaseAPIException):
    def __init__(self, message: str, missing_features: list):
        super().__init__(message=message, error_code="MISSING_FEATURES", status_code=422, details={"missing_features": missing_features})

class UnknownFeaturesException(BaseAPIException):
    def __init__(self, message: str, unknown_features: list):
        super().__init__(message=message, error_code="UNKNOWN_FEATURES", status_code=422, details={"unknown_features": unknown_features})

class ModelNotReadyException(BaseAPIException):
    def __init__(self, message: str = "Required prediction models are unavailable."):
        super().__init__(message=message, error_code="MODEL_NOT_READY", status_code=503)

class ModelLoadingException(BaseAPIException):
    def __init__(self, message: str = "Failed to load models.", details: dict = None):
        super().__init__(message=message, error_code="MODEL_LOADING_ERROR", status_code=500, details=details)
