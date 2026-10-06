from app.schemas.prediction_requests import PredictionRequest

VALID_FEATURES = PredictionRequest.model_config["json_schema_extra"]["example"]["features"]

def test_predict_failure_valid(client):
    response = client.post(
        "/api/predict/failure",
        json={"features": VALID_FEATURES}
    )
    if response.status_code == 503:
        import pytest
        pytest.skip("Models not loaded")
        
    assert response.status_code == 200
    data = response.json()
    assert "failure_prediction" in data
    assert "failure_status" in data
    assert "failure_probability" in data
    assert data["failure_prediction"] in [0, 1]
    assert 0.0 <= data["failure_probability"] <= 1.0

def test_predict_failure_missing_features(client):
    response = client.post(
        "/api/predict/failure",
        json={"features": {"manufacturing_year": 2020.0}}
    )
    if response.status_code == 503:
        import pytest
        pytest.skip("Models not loaded")
        
    assert response.status_code == 422
    data = response.json()
    assert data["error_code"] == "MISSING_FEATURES"

def test_predict_failure_malformed(client):
    response = client.post(
        "/api/predict/failure",
        json={"invalid_body": True}
    )
    assert response.status_code == 422
