
# Predictive Maintenance - Model Selection & Threshold Tuning

This notebook continues the model selection process for predictive maintenance using the AI4I 2020 dataset. It includes hyperparameter tuning, model evaluation on validation and test sets, and threshold optimization to maximize performance.

## 🔧 Model Summary

- **Model**: XGBoost Classifier
- **Hyperparameter Tuning Method**: GridSearchCV
- **Best Parameters**:
  ```json
  {
    "colsample_bytree": 0.8,
    "gamma": 0.2,
    "learning_rate": 0.1,
    "max_depth": 5,
    "min_child_weight": 1,
    "n_estimators": 200,
    "subsample": 0.8
  }
  ```

## 🧪 Threshold Tuning

Thresholds between `0.1` and `0.85` were tested to find the best trade-off between Precision and Recall. Based on F1 score on the **validation set**, the optimal threshold was:

- **Threshold**: `0.2`

This threshold was then used to evaluate final test performance.

## 📈 Final Performance Metrics

### Validation Set
- **Precision**: `0.6727`
- **Recall**: `0.7255`
- **F1 Score**: `0.6981`

### Test Set
- **Accuracy**: `0.9747`
- **Precision**: `0.6667`
- **Recall**: `0.7451`
- **F1 Score**: `0.7037`

## 🎯 Conclusion

A lower threshold (0.2) improved recall significantly, which is essential in predictive maintenance to minimize missed failures. The model maintains high accuracy and achieves a balanced F1 score, making it suitable for deployment or further integration into maintenance scheduling systems.

## 📁 File Info

- `model_selection_continued.ipynb`: Contains all training, tuning, and evaluation steps.
- `best_xgb_model.pkl`: Serialized model after tuning and evaluation.

## 🧠 Notes

- Evaluation was kept consistent with a **train/validation/test split** to avoid data leakage.
- Threshold tuning was done using **validation set only**, then applied directly on the **test set** to ensure fair evaluation.
