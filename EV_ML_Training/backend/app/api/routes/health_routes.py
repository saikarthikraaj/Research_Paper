from fastapi import APIRouter, Request
from app.api.controllers.health_controller import HealthController
from app.schemas.prediction_responses import HealthResponse

router = APIRouter()

@router.get("/health", response_model=HealthResponse)
def health_check(request: Request):
    return HealthController.get_health(request)

@router.get("/health/ready")
def readiness_check(request: Request):
    return HealthController.get_ready(request)
