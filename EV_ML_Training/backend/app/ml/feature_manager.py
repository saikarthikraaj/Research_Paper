import pandas as pd
import math
from typing import Dict, Any, List
from app.exceptions.custom_exceptions import MissingFeaturesException, UnknownFeaturesException, ValidationException

class FeatureManager:
    @staticmethod
    def validate_and_order_features(incoming_features: Dict[str, Any], expected_features: List[str]) -> pd.DataFrame:
        if incoming_features is None:
            raise ValidationException("Features dictionary cannot be null.")
            
        incoming_keys = set(incoming_features.keys())
        expected_keys = set(expected_features)

        missing = list(expected_keys - incoming_keys)
        if missing:
            raise MissingFeaturesException("Required prediction features are missing.", missing)

        unknown = list(incoming_keys - expected_keys)
        if unknown:
            raise UnknownFeaturesException("Unexpected features provided.", unknown)

        ordered_data = {}
        for feature in expected_features:
            val = incoming_features[feature]
            if type(val) == bool:
                 raise ValidationException(f"Feature '{feature}' must be numeric, got boolean.")
            if not isinstance(val, (int, float)):
                 raise ValidationException(f"Feature '{feature}' must be numeric.")
            if math.isnan(val) or math.isinf(val):
                 raise ValidationException(f"Feature '{feature}' cannot be NaN or infinity.")
            ordered_data[feature] = [val]

        # Explicitly order using expected_features list
        df = pd.DataFrame(ordered_data)
        return df[expected_features]
