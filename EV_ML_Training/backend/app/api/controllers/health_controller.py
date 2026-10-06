from fastapi import Request, HTTPException, status
from app.schemas.prediction_responses import HealthResponse
from app.ml.model_manager import ModelManager

class HealthController:
    @staticmethod
    def get_health(request: Request) -> HealthResponse:
        model_manager: ModelManager = request.app.state.model_manager
        
        models_loaded = model_manager.is_loaded if model_manager else False
        
        return HealthResponse(
            status="healthy",
            service="EV Battery Health Prediction API",
            models_loaded=models_loaded,
            classification_model_loaded=models_loaded,
            regression_model_loaded=models_loaded
        )

    @staticmethod
    def get_ready(request: Request):
        model_manager: ModelManager = request.app.state.model_manager
        
        if not model_manager or not model_manager.is_loaded:
            raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail="Models not loaded or unavailable")
            
        return {"status": "ready"}
