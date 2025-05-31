# 📄 Predictive Maintenance - Daily Progress Report (May 31, 2025)

## 🔧 Model Automation and Feature Analysis

### ✅ Summary of Today's Work

#### 1. Model Class Creation
- Developed a reusable `Model` class that automates:
  - Data splitting and scaling (`splitAndScale`)
  - Training and evaluation (`trainAndEvaluate`)
  - End-to-end execution (`run`)
- Designed to streamline the comparison of multiple ML algorithms.

#### 2. Model Evaluation
- Trained and evaluated:
  - `KNeighborsClassifier`
  - `RandomForestClassifier`
- Used key evaluation metrics:
  - Accuracy
  - Precision
  - Recall
  - F1 Score
  - Confusion Matrix

#### 3. Class Imbalance Focus
- Observed low recall despite high precision and accuracy.
- Random Forest achieved:
  - Precision: **0.91**
  - Recall: **~0.47**
  - F1 Score: **~0.62**

#### 4. Feature Importance Analysis
- Visualized feature importance using Random Forest
- Key impactful features:
  - `Rotational speed [rad/s]`
  - `Torque [Nm]`
  - `Tool wear [min]`
- Removed less important features:
  - `Power`
  - `Type (encoded)`

#### 5. Next Steps
- Address low recall with:
  - SMOTE oversampling
  - Threshold tuning
  - XGBoost or other ensemble models
