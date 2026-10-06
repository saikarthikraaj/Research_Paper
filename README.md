# 🔋 AI-Based EV Battery Health Monitoring and Failure Prediction

## 📌 Overview

This project uses **Machine Learning and Deep Learning** techniques to analyze Electric Vehicle (EV) battery data and predict battery health conditions.

The system performs two main tasks:

- 🔴 **Battery Failure Prediction** – identifies whether a battery is healthy or at risk of failure.
- 🔋 **Remaining Useful Life Prediction** – estimates the remaining battery life in charge/discharge cycles.

Different Machine Learning models are trained and compared to identify the best-performing models.

---

## 🎯 Objectives

- Analyze EV battery and vehicle parameters.
- Predict battery failure risk.
- Predict remaining battery life cycles.
- Compare Machine Learning and ANN models.
- Evaluate model performance using different metrics.
- Build a foundation for a future web-based EV battery prediction system.

---

## 🤖 Models Used

### Classification

- Random Forest
- Extra Trees
- HistGradientBoosting
- Artificial Neural Network (ANN)

### Regression

- Random Forest
- Extra Trees
- HistGradientBoosting
- Artificial Neural Network (ANN)

---

## 🏆 Best Results

### Battery Failure Classification

**Best Model: HistGradientBoosting**

| Metric | Result |
|---|---:|
| Accuracy | **96.58%** |
| Precision | 84.54% |
| Recall | **80.42%** |
| F1 Score | **82.43%** |
| Log Loss | **0.0790** |

### Remaining Life Prediction

**Best Model: Extra Trees**

| Metric | Result |
|---|---:|
| MAE | 48.82 cycles |
| RMSE | **110.41 cycles** |
| R² Score | **0.99629** |

---

## 📊 Dataset

The dataset contains EV-related parameters such as:

- Battery capacity
- State of Charge (SoC)
- State of Health (SoH)
- Cycle count
- Cell voltage
- Cell temperature
- Charging information
- Driving information
- Environmental conditions
- Battery stress and health indicators

The complete dataset is stored separately because of its large size.

📥 **Dataset:**  
[Google Drive Dataset](https://drive.google.com/drive/folders/1cRFmzwrAREaE-g6LdtkXo8LhXM3LLUdv?usp=drive_link)

---

## 📚 Research Papers

Research papers related to:

- EV Battery Management Systems
- Battery State of Charge
- Battery State of Health
- Machine Learning for Battery Prediction
- Deep Learning for Battery Health Estimation

were studied as part of this project.

📄 **Research Papers:**  
[Google Drive Research Papers](https://drive.google.com/drive/folders/1cRFmzwrAREaE-g6LdtkXo8LhXM3LLUdv?usp=drive_link)

---

## 📓 Jupyter Notebook

The complete Machine Learning implementation is available in:

```text
EV_ML_Training/EV_ML_Model.ipynb
```

The notebook includes:

- Data loading
- Data preprocessing
- Feature selection
- Missing-value handling
- Model training
- Model evaluation
- Model comparison
- Data visualization
- Battery prediction

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- TensorFlow / Keras
- Matplotlib
- Seaborn
- Jupyter Notebook
- Git & GitHub

---

## 🚀 Future Scope

The trained models can be integrated into a **React + FastAPI web application** that provides:

- Battery health prediction
- Failure probability
- Remaining life prediction
- Interactive charts
- User-friendly battery analysis dashboard

---

## 📂 Project Structure

```text
Research_Paper/
│
├── EV_ML_Training/
│   └── EV_ML_Model.ipynb
│
├── Research Papers
│
└── README.md
```

---

This version is probably the **best balance for your repository**: enough technical information for seniors/reviewers, but not unnecessarily huge.
