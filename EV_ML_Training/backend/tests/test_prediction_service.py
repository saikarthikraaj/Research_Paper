import pytest
from app.services.prediction_service import PredictionService
from app.exceptions.custom_exceptions import ModelNotReadyException
from unittest.mock import MagicMock
from app.ml.model_manager import ModelManager

def test_prediction_service_requires_loaded_models():
    mock_manager = MagicMock(spec=ModelManager)
    mock_manager.is_loaded = False
    
    with pytest.raises(ModelNotReadyException):
        PredictionService(mock_manager)

def test_prediction_service_failure_workflow():
    mock_manager = MagicMock(spec=ModelManager)
    mock_manager.is_loaded = True
    
    mock_model = MagicMock()
    mock_model.predict.return_value = [1]
    mock_model.predict_proba.return_value = [[0.1, 0.9]]
    
    mock_imputer = MagicMock()
    mock_imputer.transform.return_value = [[0] * 57]
    
    mock_manager.get_classification_artifacts.return_value = (
        mock_model,
        mock_imputer,
        ["feature_a", "feature_b"]
    )
    
    service = PredictionService(mock_manager)
    
    prediction, status, prob = service.predict_failure({"feature_a": 1.0, "feature_b": 2.0})
    
    assert prediction == 1
    assert status == "Battery Failure Risk"
    assert prob == 0.9
    mock_imputer.transform.assert_called_once()
    mock_model.predict.assert_called_once()
    mock_model.predict_proba.assert_called_once()

def test_prediction_service_regression_workflow():
    mock_manager = MagicMock(spec=ModelManager)
    mock_manager.is_loaded = True
    
    mock_model = MagicMock()
    mock_model.predict.return_value = [1500.5]
    
    mock_imputer = MagicMock()
    mock_imputer.transform.return_value = [[0] * 57]
    
    mock_manager.get_regression_artifacts.return_value = (
        mock_model,
        mock_imputer,
        ["feature_a", "feature_b"]
    )
    
    service = PredictionService(mock_manager)
    
    prediction = service.predict_remaining_life({"feature_a": 1.0, "feature_b": 2.0})
    
    assert prediction == 1500.5
    mock_imputer.transform.assert_called_once()
    mock_model.predict.assert_called_once()
