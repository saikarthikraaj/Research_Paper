from fastapi import APIRouter, Request
from app.api.controllers.prediction_controller import PredictionController
from app.schemas.prediction_requests import PredictionRequest
from app.schemas.prediction_responses import ClassificationResponse, RegressionResponse
from app.schemas.common import ErrorResponse

router = APIRouter(prefix="/api/predict", tags=["prediction"])

@router.post(
    "/failure", 
    response_model=ClassificationResponse,
    responses={
        422: {"model": ErrorResponse},
        400: {"model": ErrorResponse},
        500: {"model": ErrorResponse},
        503: {"model": ErrorResponse},
    }
)
def predict_failure(request: Request, payload: PredictionRequest):
    return PredictionController.predict_failure(request, payload)

@router.post(
    "/remaining-life", 
    response_model=RegressionResponse,
    responses={
        422: {"model": ErrorResponse},
        400: {"model": ErrorResponse},
        500: {"model": ErrorResponse},
        503: {"model": ErrorResponse},
    }
)
def predict_remaining_life(request: Request, payload: PredictionRequest):
    return PredictionController.predict_remaining_life(request, payload)
