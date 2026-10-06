import httpx
import time
import sys

URL = "http://127.0.0.1:8000"

print("Waiting for server to be ready...")
for _ in range(30):
    try:
        res = httpx.get(f"{URL}/health/ready")
        if res.status_code == 200:
            print("Server is ready!")
            break
    except Exception:
        pass
    time.sleep(1)
else:
    print("Server did not become ready.")
    sys.exit(1)

print("\n--- Testing GET /health ---")
r = httpx.get(f"{URL}/health")
print(f"Status: {r.status_code}")
print(r.json())

print("\n--- Testing GET /docs ---")
r = httpx.get(f"{URL}/docs")
print(f"Status: {r.status_code}")

print("\n--- Testing POST /api/predict/failure ---")
sample_features = {
    "manufacturing_year": 2020.0,
    "battery_capacity_kwh": 75.0,
    "odometer_km": 50000.0,
    "vehicle_age_years": 3.0,
    "cycle_count": 300.0,
    "battery_health_percent": 90.0,
    "state_of_charge": 80.0,
    "depth_of_discharge": 20.0,
    "state_of_health": 95.0,
    "cell_voltage_avg": 3.7,
    "cell_voltage_std": 0.01,
    "pack_voltage": 400.0,
    "cell_temperature_avg": 25.0,
    "cell_temperature_max": 30.0,
    "internal_resistance": 0.05,
    "charge_efficiency": 95.0,
    "discharge_efficiency": 94.0,
    "remaining_capacity": 70.0,
    "capacity_loss_percent": 5.0,
    "charging_cycles_last_month": 15.0,
    "fast_charge_ratio": 0.2,
    "average_charge_power_kw": 50.0,
    "average_charging_time": 60.0,
    "charging_interruptions": 1.0,
    "overcharge_events": 0.0,
    "average_speed": 60.0,
    "average_trip_distance": 40.0,
    "aggressive_acceleration_score": 2.0,
    "hard_braking_score": 1.5,
    "regenerative_braking_usage": 0.8,
    "highway_driving_ratio": 0.6,
    "city_driving_ratio": 0.4,
    "daily_distance": 50.0,
    "average_ambient_temperature": 20.0,
    "maximum_temperature": 35.0,
    "minimum_temperature": 0.0,
    "humidity": 50.0,
    "altitude": 100.0,
    "dust_exposure": 0.1,
    "last_service_days": 180.0,
    "cooling_system_health": 98.0,
    "firmware_updates": 5.0,
    "previous_faults": 0.0,
    "maintenance_score": 9.5,
    "thermal_runaway_risk": 0.01,
    "voltage_imbalance": 0.02,
    "temperature_variance": 1.5,
    "sensor_fault_count": 0.0,
    "BMS_warning_count": 0.0,
    "abnormal_voltage_events": 0.0,
    "battery_stress_index": 0.1,
    "aging_score": 0.2,
    "thermal_health_score": 99.0,
    "charging_quality_score": 95.0,
    "driving_stress_score": 1.0,
    "vehicle_brand_encoded": 1.0,
    "vehicle_model_encoded": 2.0
}
r = httpx.post(f"{URL}/api/predict/failure", json={"features": sample_features})
print(f"Status: {r.status_code}")
print(r.json())

print("\n--- Testing POST /api/predict/remaining-life ---")
r = httpx.post(f"{URL}/api/predict/remaining-life", json={"features": sample_features})
print(f"Status: {r.status_code}")
print(r.json())
