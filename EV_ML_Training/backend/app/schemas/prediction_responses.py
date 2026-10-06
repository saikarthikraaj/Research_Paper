from pydantic import BaseModel

class HealthResponse(BaseModel):
    status: str
    service: str
    models_loaded: bool
    classification_model_loaded: bool
    regression_model_loaded: bool

class ClassificationResponse(BaseModel):
    failure_prediction: int
    failure_status: str
    failure_probability: float

class RegressionResponse(BaseModel):
    predicted_remaining_life_cycles: float
