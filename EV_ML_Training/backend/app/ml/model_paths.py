import os
from pathlib import Path
from app.config.settings import settings

def get_project_root() -> Path:
    # Resolves to the backend directory
    return Path(__file__).resolve().parent.parent.parent

def get_model_dir() -> Path:
    return (get_project_root() / settings.MODEL_DIR).resolve()

MODEL_DIR = get_model_dir()

CLASSIFICATION_MODEL_PATH = MODEL_DIR / "hist_gradient_boosting_model.pkl"
REGRESSION_MODEL_PATH = MODEL_DIR / "extra_trees_regression_model.pkl"
CLASSIFICATION_IMPUTER_PATH = MODEL_DIR / "imputer.pkl"
REGRESSION_IMPUTER_PATH = MODEL_DIR / "regression_imputer.pkl"
CLASSIFICATION_FEATURES_PATH = MODEL_DIR / "features.pkl"
REGRESSION_FEATURES_PATH = MODEL_DIR / "regression_features.pkl"
