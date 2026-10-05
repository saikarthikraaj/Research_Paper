# 🔋 AI-Based EV Battery Health Monitoring and Failure Prediction System

## 📌 Project Overview

The **AI-Based EV Battery Health Monitoring and Failure Prediction System** is a software-based Machine Learning project designed to analyze Electric Vehicle (EV) battery and vehicle parameters and predict battery failure risk.

The system uses an EV predictive-maintenance dataset and Machine Learning to classify the condition as **Normal** or **Failure Risk**.

The project will later integrate the trained model with a **FastAPI backend** and **React frontend** to create an interactive EV battery monitoring dashboard.

> **Note:** This is a completely software-based project. No Arduino, ESP32, IoT sensors, or physical battery hardware are used.

---

## 🎯 Objectives

- Analyze EV battery and vehicle parameters.
- Predict battery failure risk using Machine Learning.
- Monitor battery parameters such as SoC, SoH, voltage, current, and temperature.
- Provide AI-based failure prediction.
- Display battery health and failure-risk analytics through a web dashboard.

---

## 📊 Dataset

The project uses the **EV Predictive Maintenance Dataset**.

- **Records:** 175,393
- **Columns:** 30
- **Target:** `Failure_Probability`

### Target Classes

- `0` → Normal
- `1` → Failure Risk

### Important Features

- SoC
- SoH
- Battery Voltage
- Battery Current
- Battery Temperature
- Charge Cycles
- Motor Temperature
- Motor Vibration
- Motor RPM
- Power Consumption
- Driving Speed
- Distance Traveled
- RUL
- Failure Probability
- Component Health Score

### 📥 Dataset Drive Link

**[Open Dataset – Google Drive](https://drive.google.com/drive/folders/1cRFmzwrAREaE-g6LdtkXo8LhXM3LLUdv?usp=drive_link)**

---

## 🤖 Machine Learning

Several classification models were tested:

1. Logistic Regression
2. Scaled Logistic Regression
3. HistGradientBoostingClassifier
4. HistGradientBoostingClassifier with Class Balancing

### 🏆 Final Model

**HistGradientBoostingClassifier with class balancing**

The model uses **24 input features** to predict:

**Normal / Failure Risk**

### Model Performance

| Metric | Score |
|---|---:|
| Accuracy | 59.58% |
| Precision | 10.33% |
| Recall | 40.25% |
| F1-Score | 16.44% |
| Log Loss | 0.689 |

### Saved Model Files

```text
battery_failure_model.pkl
battery_features.pkl
````

---

## 📈 Data & Model Visualizations

The project includes:

* Failure Risk Distribution
* Model Performance Comparison
* Confusion Matrix
* SoH Distribution
* Battery Temperature Distribution
* SoH vs Battery Temperature

---

## 🌐 Web Application

The trained Machine Learning model will be integrated into a web application using:

**React → FastAPI → Machine Learning Model**

### Planned Pages

* Dashboard
* Battery Analysis
* AI Prediction
* Analytics
* Alerts
* Model Performance
* About

### Dashboard

The dashboard will display:

* State of Health (SoH)
* State of Charge (SoC)
* Battery Temperature
* Failure Risk
* Battery Voltage
* Battery Current
* Charge Cycles
* Motor Temperature
* Power Consumption
* Battery health charts
* Failure-risk charts

### AI Prediction

Users will enter battery and vehicle parameters.

The data will be sent to the FastAPI backend, which will use the trained Machine Learning model to return:

**Normal** or **Failure Risk**

---

## 🏗️ System Workflow

```text
EV Predictive Maintenance Dataset
              ↓
       Data Preprocessing
              ↓
        Feature Selection
              ↓
       Machine Learning
              ↓
        Model Evaluation
              ↓
       Trained ML Model
              ↓
        FastAPI Backend
              ↓
         React Frontend
              ↓
      EV Battery Dashboard
```

---

## 🛠️ Technology Stack

### Machine Learning

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* Jupyter Notebook

### Backend

* Python
* FastAPI
* Uvicorn
* Joblib

### Frontend

* React
* JavaScript
* HTML
* CSS

### Tools

* VS Code
* Jupyter Notebook
* Git
* GitHub

---

## 📁 Project Structure

```text
EVProject/
│
├── battery.ipynb
├── battery_failure_model.pkl
├── battery_features.pkl
│
├── backend/
│   └── main.py
│
└── frontend/
    └── React Application
```

The large dataset is stored separately on Google Drive.

---

## 📚 Research Papers

Research papers related to EV battery health, State of Charge (SoC), State of Health (SoH), battery degradation, Machine Learning, Deep Learning, and Battery Management Systems are used as references for this project.

### 📖 Research Papers Drive Link

**[Open Research Papers – Google Drive](https://drive.google.com/drive/folders/1heVwKE3r1Kocon-JM1tv4IdILVGsxuYb)**

---

## 🔬 Research Areas

The collected research papers cover areas such as:

* EV Battery SoC Estimation
* EV Battery SoH Estimation
* Lithium-Ion Battery Health Prediction
* Battery Degradation
* Machine Learning for Battery Prediction
* Deep Learning for Battery Prediction
* Battery Management Systems
* Battery Failure Prediction
* Predictive Maintenance

---

## ✅ Project Status

### Completed

* [x] Dataset Collection
* [x] Dataset Analysis
* [x] Data Preprocessing
* [x] Feature Selection
* [x] Model Training
* [x] Model Comparison
* [x] Model Evaluation
* [x] Confusion Matrix
* [x] Data Visualization
* [x] Model Saving
* [x] Research Paper Collection

### In Progress

* [ ] FastAPI Backend
* [ ] Prediction API
* [ ] React Frontend
* [ ] Dashboard
* [ ] AI Prediction Page
* [ ] Analytics Page
* [ ] Alerts Page
* [ ] Model Performance Page

---

## 🔮 Future Enhancements

* Improve model performance
* Add Remaining Useful Life (RUL) prediction
* Add battery degradation prediction
* Add anomaly detection
* Add additional datasets
* Deploy the application to the cloud
* Implement automatic model retraining

---

## ⚠️ Project Scope

This project is completely software-based.

It does **not** use:

* Arduino
* ESP32
* IoT sensors
* Physical EV batteries
* Hardware-based data collection

The system uses an existing EV dataset for Machine Learning analysis and prediction.

---

### GitHub

**[GitHub Profile](https://github.com/saikarthikraaj)**

### Project Repository

**[Research Paper Repository](https://github.com/saikarthikraaj/Research_Paper)**

---

## 📄 License

This project is developed for **educational and research purposes**.

```

This version is ready to paste directly into your **GitHub `README.md`**.
```
