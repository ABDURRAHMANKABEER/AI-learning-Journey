# 🛠️ Predictive Maintenance in Oil and Gas Using Machine Learning
This project explores the application of machine learning techniques to predict machine failures using real-world industrial sensor data. It is part of my journey into AI-driven reliability engineering, specifically for oil and gas operations, and contributes to a proposed research paper for the Society of Petroleum Engineers (SPE) paper contest.

**📊 Dataset**
Name: AI4I 2020 Predictive Maintenance Dataset

Size: 10,000 rows, 14 columns

Source: UCI Machine Learning Repository

Each data point captures the physical operating conditions of a machine, including:

Air temperature, Process temperature

Rotational speed, Torque, Tool wear

Five types of machine failures (TWF, HDF, PWF, OSF, RNF)

A binary Machine failure label used for training predictive models

## 🎯 Project Objectives
✅ Perform thorough data cleaning and preprocessing

✅ Visualize distributions, detect potential outliers, and understand data behavior

✅ Conduct feature-target correlation analysis

✅ Train and evaluate various ML models for predictive performance

✅ Compare model results and select the most reliable

✅ Analyze failure causes based on sensor behavior

**🔍 Why This Matters**
In oil and gas, unscheduled downtime due to equipment failure results in high economic loss and safety risks. Predictive maintenance minimizes this by using real-time data to anticipate faults before they happen.

## 🚀 Tech Stack
Python, pandas, numpy

matplotlib, seaborn

scikit-learn

Jupyter Notebook

## 🧪 Models Tried
- Logistic Regression
- Random Forest
- XGBoost with SMOTE + `scale_pos_weight`
- Threshold Tuning for Precision/Recall balance

---

## 🔍 Key Findings
- F1 score peaked at ~66% with SMOTE + XGBoost
- Precision–Recall tradeoff is challenging
- Threshold tuning improved recall at the cost of precision
- Best threshold (~0.7) gave:
  - ✅ Precision ≈ 76%
  - ✅ Recall ≈ 66%

---

## 📊 Model Log
See `model_log.md` for all test scores, confusion matrices, and thresholds tried.

---

## 🚀 Next Steps
- Split into train/validation/test properly
- Avoid overfitting by using validation for threshold tuning
- Try stacking / ensemble learning
- Deploy as a Flask or Streamlit app (optional)

---

## 👤 Author
**Abdurrahman Kabir**  
Electrical Engineering Student, Ahmadu Bello University Zaria
Aspiring AI & Control Systems Engineer
[LinkedIn](https://www.linkedin.com/in/abdurrahman-kabir-10580220b) | [GitHub](https://github.com/ABDURRAHMANKABEER)