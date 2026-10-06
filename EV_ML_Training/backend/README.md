# EV Battery Health Prediction API

This is a stateless ML inference FastAPI backend for EV Battery Health Prediction. 

## Purpose
Provides a production-grade layered API architecture for battery health failure and remaining life predictions. It is designed to be used by a future React frontend.

## Limitations
- **Inference Only**: This backend does not retrain, replace, or modify any ML models.
- **Stateless**: No database, Redis, or Celery. Predictions are processed synchronously and statelessly.

## Architecture
- `app/api/routes`: FastAPI route definitions.
- `app/api/controllers`: HTTP request/response handlers.
- `app/services`: Core prediction workflows and business logic.
- `app/ml`: Model loading, path resolution, and feature validation.
- `app/schemas`: Pydantic request/response and error models.
- `app/middleware`: Centralized error handling, request ID assignment, and request logging.
- `app/exceptions`: Custom application exceptions.
- `app/utils`: Reusable configuration, such as logging.

## Required Environment (Windows)
It is recommended to use the existing `EV ML Python` environment to ensure scikit-learn version compatibility (`scikit-learn==1.7.2`).

```bash
# If you don't have it, create one:
python -m venv venv
.\venv\Scripts\activate
```

## Installation
```bash
pip install -r requirements.txt
```

## Configuration
Copy `.env.example` to `.env` and adjust the settings. The `MODEL_DIR` should point to the relative directory where the `.pkl` files are stored (default is `../saved_model`).

## Model Artifacts
The application requires six files in `MODEL_DIR`:
1. `hist_gradient_boosting_model.pkl`: Classification model
2. `extra_trees_regression_model.pkl`: Regression model
3. `imputer.pkl`: Classification imputer
4. `regression_imputer.pkl`: Regression imputer
5. `features.pkl`: Classification features list
6. `regression_features.pkl`: Regression features list

## Running the API
Start the server from the `backend` directory:
```bash
python -m uvicorn app.main:app --reload
```

## URLs
- **Swagger Docs**: http://127.0.0.1:8000/docs
- **Redoc**: http://127.0.0.1:8000/redoc
- **Health**: http://127.0.0.1:8000/health
- **Ready**: http://127.0.0.1:8000/health/ready

## Example Requests

### Classification (Failure Prediction)
```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/predict/failure" -Method Post -Headers @{"Content-Type"="application/json"} -Body '{"features": {"manufacturing_year": 2020.0, "battery_capacity_kwh": 75.0, "odometer_km": 50000.0, "vehicle_age_years": 3.0, "cycle_count": 300.0, "battery_health_percent": 90.0, "state_of_charge": 80.0, "depth_of_discharge": 20.0, "state_of_health": 95.0, "cell_voltage_avg": 3.7, "cell_voltage_std": 0.01, "pack_voltage": 400.0, "cell_temperature_avg": 25.0, "cell_temperature_max": 30.0, "internal_resistance": 0.05, "charge_efficiency": 95.0, "discharge_efficiency": 94.0, "remaining_capacity": 70.0, "capacity_loss_percent": 5.0, "charging_cycles_last_month": 15.0, "fast_charge_ratio": 0.2, "average_charge_power_kw": 50.0, "average_charging_time": 60.0, "charging_interruptions": 1.0, "overcharge_events": 0.0, "average_speed": 60.0, "average_trip_distance": 40.0, "aggressive_acceleration_score": 2.0, "hard_braking_score": 1.5, "regenerative_braking_usage": 0.8, "highway_driving_ratio": 0.6, "city_driving_ratio": 0.4, "daily_distance": 50.0, "average_ambient_temperature": 20.0, "maximum_temperature": 35.0, "minimum_temperature": 0.0, "humidity": 50.0, "altitude": 100.0, "dust_exposure": 0.1, "last_service_days": 180.0, "cooling_system_health": 98.0, "firmware_updates": 5.0, "previous_faults": 0.0, "maintenance_score": 9.5, "thermal_runaway_risk": 0.01, "voltage_imbalance": 0.02, "temperature_variance": 1.5, "sensor_fault_count": 0.0, "BMS_warning_count": 0.0, "abnormal_voltage_events": 0.0, "battery_stress_index": 0.1, "aging_score": 0.2, "thermal_health_score": 99.0, "charging_quality_score": 95.0, "driving_stress_score": 1.0, "vehicle_brand_encoded": 1.0, "vehicle_model_encoded": 2.0}}'
```

## Running Tests
```bash
pytest
```
