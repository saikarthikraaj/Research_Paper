from fastapi import Request
from app.schemas.prediction_requests import PredictionRequest
from app.schemas.prediction_responses import ClassificationResponse, RegressionResponse
from app.services.prediction_service import PredictionService
from app.ml.model_manager import ModelManager

class PredictionController:
    @staticmethod
    def predict_failure(request: Request, payload: PredictionRequest) -> ClassificationResponse:
        model_manager: ModelManager = request.app.state.model_manager
        service = PredictionService(model_manager)
        
        prediction, failure_status, failure_probability = service.predict_failure(payload.features)
        
        return ClassificationResponse(
            failure_prediction=prediction,
            failure_status=failure_status,
            failure_probability=failure_probability
        )

    @staticmethod
    def predict_remaining_life(request: Request, payload: PredictionRequest) -> RegressionResponse:
        model_manager: ModelManager = request.app.state.model_manager
        service = PredictionService(model_manager)
        
        prediction = service.predict_remaining_life(payload.features)
        
        return RegressionResponse(
            predicted_remaining_life_cycles=prediction
        )
