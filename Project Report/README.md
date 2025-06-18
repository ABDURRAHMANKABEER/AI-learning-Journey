# From Breakdown to Breakthrough  
### AI Reliability and Maintainability in Oil and Gas

---

## 1. Introduction: Why This Project?
This project explores how AI can be used to predict machine failures before they happen using real-time sensor data.  
The dataset, AI4I 2020, simulates industrial machinery monitored under various conditions. Predictive maintenance is  
critical in high-risk industries like oil and gas, where failures can cost millions or lead to hazardous incidents.

---

## 2. Understanding the Data
The dataset consists of 10,000 rows and 14 columns including temperature, rotational speed, torque, and tool wear.  
A key early discovery was that the data was imbalanced — only a small percentage of machines failed.  
Feature engineering and correlation analysis helped reduce redundancy, such as using `power = torque × speed` instead  
of keeping both separately.

---

## 3. Modeling Approach
I started with baseline models like Logistic Regression and K-Nearest Neighbors before moving to more complex models  
like Random Forest and XGBoost. The class imbalance was addressed using XGBoost’s `scale_pos_weight` parameter,  
and model selection was done using precision, recall, and F1 score.

---

## 4. Hyperparameter Tuning
Using `RandomizedSearchCV`, I tested 648 combinations over 5-fold cross-validation. The best configuration included:
- `learning_rate = 0.1`
- `max_depth = 5`
- `n_estimators = 200`
- `gamma = 0.2`
- `colsample_bytree = 0.8`  
This tuning improved model robustness and generalization.

---

## 5. Threshold Tuning
While the model performed well, the default threshold of 0.5 didn't meet operational goals.  
I applied threshold tuning using validation data and found that lowering the threshold to 0.2 provided the best F1 balance.  
This helped capture more failures (higher recall) while keeping precision acceptable.

---

## 6. Final Performance
With `threshold = 0.2`, the final evaluation metrics on the **test set** were:
- **Accuracy**: 97.47%  
- **Precision**: 61.0%  
- **Recall**: 70.6%  
- **F1 Score**: 65.4%  

These metrics show that the model is ready for real-world experimentation or further refinement.

---

## 7. Lessons Learned
This project taught me that model building is only part of the challenge.  
I learned how to evaluate and tune models based on business needs (e.g., cost of false positives vs. false negatives).  
I also learned the importance of data splits, proper testing, and how to visualize trade-offs like precision vs. recall.

---

## 8. What's Next
The journey is far from over.  
My next step is to test this model on real-world predictive maintenance datasets from the oil and gas industry.  
I also plan to take this project further by applying deep learning techniques such as LSTMs or CNNs for time series data,  
and eventually contribute it as a technical paper for SPE competitions.
