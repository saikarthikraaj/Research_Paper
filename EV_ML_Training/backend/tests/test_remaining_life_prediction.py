from app.schemas.prediction_requests import PredictionRequest
import math

VALID_FEATURES = PredictionRequest.model_config["json_schema_extra"]["example"]["features"]

def test_predict_remaining_life_valid(client):
    response = client.post(
        "/api/predict/remaining-life",
        json={"features": VALID_FEATURES}
    )
    if response.status_code == 503:
        import pytest
        pytest.skip("Models not loaded")
        
    assert response.status_code == 200
    data = response.json()
    assert "predicted_remaining_life_cycles" in data
    assert isinstance(data["predicted_remaining_life_cycles"], (int, float))
    assert not math.isnan(data["predicted_remaining_life_cycles"])
    assert not math.isinf(data["predicted_remaining_life_cycles"])

def test_predict_remaining_life_unknown_features(client):
    invalid_features = VALID_FEATURES.copy()
    invalid_features["some_unknown_feature"] = 123.0
    
    response = client.post(
        "/api/predict/remaining-life",
        json={"features": invalid_features}
    )
    if response.status_code == 503:
        import pytest
        pytest.skip("Models not loaded")
        
    assert response.status_code == 422
    data = response.json()
    assert data["error_code"] == "UNKNOWN_FEATURES"
