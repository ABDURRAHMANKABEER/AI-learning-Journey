# Machine Failure Prediction (Balanced Dataset)

This project aims to build a machine learning model that predicts machine failures using real-world sensor data with a nearly balanced target class distribution.

---

## 📊 Dataset Overview

- **Rows**: 944  
- **Features**: 9 sensor + contextual variables (e.g. `footfall`, `CS`, `RP`, `IP`, `Temperature`, etc.)  
- **Target**: `fail` (binary classification)  
- **Balance**: `fail=0`: 551, `fail=1`: 393 (no need for SMOTE or scale_pos_weight)

---

## 🔧 Project Workflow

### 1. **Exploratory Data Analysis (EDA)**
- Checked nulls, datatypes, and basic distributions.
- Used histograms and boxplots to assess outliers.
- Found `footfall` slightly skewed but not removed (tree models used).

### 2. **Feature Insights**
Each feature was interpreted from a domain perspective to confirm its relevance:
- `CS`, `RP`, `IP`, and `Temperature` are **strong predictors** of physical stress.
- `VOC`, `AQ`, and `USS` reflect environmental risks.
- `footfall` and `tempMode` included but treated cautiously.

### 3. **Custom Modeling Class**
Created a reusable ML class with:
- Train/Validation/Test splitting (70/15/15)
- Optional scaling (enabled by default)
- Model training, evaluation, and logging

### 4. **Model Training (XGBoost)**
- Used `StandardScaler`
- No class reweighting needed (balanced dataset)
- Evaluated on both validation and test sets

### 5. **Hyperparameter Tuning**
- `GridSearchCV` with:
  - `max_depth`, `learning_rate`, `n_estimators`
  - `gamma`, `subsample`, `colsample_bytree`
- Refit based on `f1` score

---

## ✅ Final Results

### 🔍 Validation Set:
- **Accuracy**: 0.9507  
- **Precision**: 0.9483  
- **Recall**: 0.9322  
- **F1 Score**: 0.9402

### 🧪 Test Set:
- **Accuracy**: 0.8873  
- **Precision**: 0.8644  
- **Recall**: 0.8644  
- **F1 Score**: 0.8644

### 🔧 Best Hyperparameters:
```
colsample_bytree=1.0
gamma=0.3
learning_rate=0.2
max_depth=5
n_estimators=100
subsample=1.0
random_state=42
```

---

## 📁 Files Included
- `model_training.ipynb` — core code and model evaluation
- `model_log.csv` — logs each model’s performance
- `README.md` — summary of approach and findings

---

## 🚀 What’s Next
- Move on to regression modeling (house prices, equipment life, etc.)
- Explore deep learning methods (MLPs, CNNs, LSTMs)
- Extend this model for real-time inference or dashboard integration

---

*Completed on: 2025-06-18*  
*Author: Abdurrahman Kabir*
