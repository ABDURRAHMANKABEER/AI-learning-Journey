# Predictive Maintenance - Day 1 Progress

## ✅ Model: Logistic Regression

### 🛠️ Preprocessing:
- Features scaled using `StandardScaler`
- Target: `machine_failure`
- Removed `torque` and `rotational_speed`, used `power` instead

### ⚙️ Model Parameters:
- `class_weight='balanced'`
- `random_state=42`

### 📊 Results (Test Set):
- **Accuracy:** 0.7305
- **Precision:** 0.0974
- **Recall:** 0.8382
- **F1 Score:** 0.1746

### 🔍 Confusion Matrix:
        Predicted
           | 0  |  1
      ----------------
Actual | 0 |1404| 528
       | 1 | 11 | 57


### 🧠 Interpretation:
- High recall: Most failures were detected (TP = 57, FN = 11)
- Very low precision: 528 false alarms out of 585 predicted failures
- This model is **sensitive** to failure, but not **specific**
- Suitable as a **baseline model**; will be improved in future iterations
