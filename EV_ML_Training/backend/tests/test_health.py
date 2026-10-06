def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["service"] == "EV Battery Health Prediction API"
    assert "models_loaded" in data

def test_readiness_check(client):
    response = client.get("/health/ready")
    if response.status_code == 200:
        assert response.json() == {"status": "ready"}
    else:
        assert response.status_code == 503
