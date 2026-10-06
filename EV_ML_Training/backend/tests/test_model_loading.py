import pytest
from app.ml.model_manager import ModelManager

def test_model_manager_initialization():
    manager = ModelManager()
    assert manager.is_loaded == False

def test_model_loading_failure_with_missing_files(monkeypatch):
    manager = ModelManager()
    
    monkeypatch.setattr("pathlib.Path.exists", lambda self: False)
    
    from app.exceptions.custom_exceptions import ModelLoadingException
    with pytest.raises(ModelLoadingException):
        manager.load_models()
        
    assert manager.is_loaded == False
