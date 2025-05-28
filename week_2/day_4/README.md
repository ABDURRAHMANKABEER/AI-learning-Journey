# 📅 Model Development Log – Day X: K-Nearest Neighbors (KNN)

## ✅ Objective:
Test the performance of a **K-Nearest Neighbors (KNN)** classifier on selected features (`tool_wear`, `power`) to predict machine failure.

---

## ⚙️ Steps Completed:

1. **Cross-validation and parameter tuning**
   - Visualized performance across different K values
   - Observed performance peak at odd K values (e.g., K=5)

2. **Model Training**
   - Used `KNeighborsClassifier` with `n_neighbors=5`
   - Scaled the features using `StandardScaler`
   - Trained on scaled `tool_wear` and `power`

3. **Performance Metrics**
   - Accuracy: `0.981`
   - Precision: `0.8286`
   - Recall: `0.4754` ⬅️ **Critical insight**: Low recall = model is missing many actual failures
   - F1 Score: `0.6041`

4. **Visualization**
   - Plotted decision boundary for KNN using the 2 selected features
   - Observed tight boundary but many failure samples are misclassified

5. **Findings**
   - Recall is still low — major concern in predictive maintenance
   - Data is imbalanced (few failures) and simple models like KNN may not generalize well
   - Plan to try **more powerful models (Random Forest, XGBoost)** in the next session

---

## 📝 Conclusion:
KNN performs decently in precision and accuracy but struggles with recall. We suspect this is due to:
- **Data imbalance** (rare failure cases)
- **Model simplicity** (KNN can't model complex relationships)

📌 **Next step**: Try `RandomForestClassifier` with `class_weight='balanced'`
