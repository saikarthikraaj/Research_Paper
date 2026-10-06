from app.ml.model_manager import ModelManager
from app.ml.feature_manager import FeatureManager
from app.exceptions.custom_exceptions import ModelNotReadyException
from typing import Dict, Any, Tuple

class PredictionService:
    def __init__(self, model_manager: ModelManager):
        self.model_manager = model_manager
        if not self.model_manager or not self.model_manager.is_loaded:
            raise ModelNotReadyException()

    def predict_failure(self, features: Dict[str, Any]) -> Tuple[int, str, float]:
        model, imputer, expected_features = self.model_manager.get_classification_artifacts()
        
        df = FeatureManager.validate_and_order_features(features, expected_features)
        
        X_imputed = imputer.transform(df)
        
        prediction = int(model.predict(X_imputed)[0])
        probabilities = model.predict_proba(X_imputed)[0]
        
        # class 1 probability
        failure_prob = float(probabilities[1])
        
        status = "Battery Failure Risk" if prediction == 1 else "Battery Healthy"
        
        return prediction, status, failure_prob

    def predict_remaining_life(self, features: Dict[str, Any]) -> float:
        model, imputer, expected_features = self.model_manager.get_regression_artifacts()
        
        df = FeatureManager.validate_and_order_features(features, expected_features)
        
        X_imputed = imputer.transform(df)
        
        prediction = float(model.predict(X_imputed)[0])
        
        return prediction
