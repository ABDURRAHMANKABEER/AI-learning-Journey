# Model Training Log

## Dataset:
- AI4I 2020 Predictive Maintenance Dataset
- Shape: (10,000, 14)

---

## Model 1: Logistic Regression (Baseline)
- Accuracy: 0.92
- Precision: 0.10
- Recall: 0.85
- F1 Score: 0.18

---

## Model 2: XGBoost + SMOTE
- Threshold: 0.7
- Precision: 0.76
- Recall: 0.66
- F1 Score: 0.70

Notes:
- Best balance observed at 0.7 threshold
- Higher thresholds increased precision but dropped recall
