import joblib
import logging
from app.ml.model_paths import (
    CLASSIFICATION_MODEL_PATH,
    REGRESSION_MODEL_PATH,
    CLASSIFICATION_IMPUTER_PATH,
    REGRESSION_IMPUTER_PATH,
    CLASSIFICATION_FEATURES_PATH,
    REGRESSION_FEATURES_PATH
)
from app.exceptions.custom_exceptions import ModelLoadingException
from app.utils.logging_config import logger

class ModelManager:
    def __init__(self):
        self.classification_model = None
        self.regression_model = None
        self.classification_imputer = None
        self.regression_imputer = None
        self.classification_features = None
        self.regression_features = None
        self.is_loaded = False
        
    def load_models(self):
        try:
            logger.info("Starting model loading process...")
            
            # Check existence
            for path in [CLASSIFICATION_MODEL_PATH, REGRESSION_MODEL_PATH, 
                         CLASSIFICATION_IMPUTER_PATH, REGRESSION_IMPUTER_PATH, 
                         CLASSIFICATION_FEATURES_PATH, REGRESSION_FEATURES_PATH]:
                if not path.exists():
                    logger.error(f"Missing required model file: {path}")
                    raise ModelLoadingException(f"Missing required model file.")

            # Load feature lists
            self.classification_features = joblib.load(CLASSIFICATION_FEATURES_PATH)
            self.regression_features = joblib.load(REGRESSION_FEATURES_PATH)
            
            if not isinstance(self.classification_features, (list, tuple, set)) or not isinstance(self.regression_features, (list, tuple, set)):
                raise ModelLoadingException("Feature lists must be an ordered collection.")
            
            # Convert to list to ensure order preservation and list properties
            self.classification_features = list(self.classification_features)
            self.regression_features = list(self.regression_features)

            # Load imputers
            self.classification_imputer = joblib.load(CLASSIFICATION_IMPUTER_PATH)
            self.regression_imputer = joblib.load(REGRESSION_IMPUTER_PATH)
            
            if not hasattr(self.classification_imputer, 'transform') or not hasattr(self.regression_imputer, 'transform'):
                raise ModelLoadingException("Imputers must support transform().")

            # Load models
            self.classification_model = joblib.load(CLASSIFICATION_MODEL_PATH)
            self.regression_model = joblib.load(REGRESSION_MODEL_PATH)

            if not hasattr(self.classification_model, 'predict') or not hasattr(self.classification_model, 'predict_proba'):
                raise ModelLoadingException("Classification model must support predict() and predict_proba().")
                
            if not hasattr(self.regression_model, 'predict'):
                raise ModelLoadingException("Regression model must support predict().")

            self.is_loaded = True
            logger.info("All models and artifacts loaded and validated successfully.")
            
        except ModelLoadingException as e:
            self.is_loaded = False
            raise e
        except Exception as e:
            self.is_loaded = False
            logger.error(f"Unexpected error loading models: {e}", exc_info=True)
            raise ModelLoadingException(f"Unexpected error loading models: {e}")

    def get_classification_artifacts(self):
        if not self.is_loaded:
            raise ModelLoadingException("Models are not loaded.")
        return self.classification_model, self.classification_imputer, self.classification_features

    def get_regression_artifacts(self):
        if not self.is_loaded:
            raise ModelLoadingException("Models are not loaded.")
        return self.regression_model, self.regression_imputer, self.regression_features
