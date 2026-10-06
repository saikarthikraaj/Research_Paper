import pytest
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixture
def client():
    # Because of FastAPI lifespan, we should use TestClient with a with-block
    # But for simple unit tests we can just return it if we mock state
    with TestClient(app) as client:
        yield client
