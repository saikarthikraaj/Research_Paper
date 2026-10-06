import pytest
from app.ml.feature_manager import FeatureManager
from app.exceptions.custom_exceptions import ValidationException, MissingFeaturesException, UnknownFeaturesException
import math

def test_missing_features():
    incoming = {"a": 1}
    expected = ["a", "b"]
    with pytest.raises(MissingFeaturesException):
        FeatureManager.validate_and_order_features(incoming, expected)

def test_unknown_features():
    incoming = {"a": 1, "b": 2, "c": 3}
    expected = ["a", "b"]
    with pytest.raises(UnknownFeaturesException):
        FeatureManager.validate_and_order_features(incoming, expected)

def test_invalid_boolean_feature():
    incoming = {"a": True, "b": 2}
    expected = ["a", "b"]
    with pytest.raises(ValidationException, match="must be numeric, got boolean"):
        FeatureManager.validate_and_order_features(incoming, expected)

def test_invalid_string_feature():
    incoming = {"a": "1", "b": 2}
    expected = ["a", "b"]
    with pytest.raises(ValidationException, match="must be numeric"):
        FeatureManager.validate_and_order_features(incoming, expected)

def test_nan_feature():
    incoming = {"a": math.nan, "b": 2}
    expected = ["a", "b"]
    with pytest.raises(ValidationException, match="cannot be NaN or infinity"):
        FeatureManager.validate_and_order_features(incoming, expected)

def test_infinity_feature():
    incoming = {"a": math.inf, "b": 2}
    expected = ["a", "b"]
    with pytest.raises(ValidationException, match="cannot be NaN or infinity"):
        FeatureManager.validate_and_order_features(incoming, expected)

def test_valid_features_ordering():
    incoming = {"b": 2.0, "a": 1.0}
    expected = ["a", "b"]
    df = FeatureManager.validate_and_order_features(incoming, expected)
    assert list(df.columns) == expected
    assert df.iloc[0]["a"] == 1.0
    assert df.iloc[0]["b"] == 2.0
