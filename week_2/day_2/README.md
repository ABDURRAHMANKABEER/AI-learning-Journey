
# Day 5 - Feature Selection & Correlation Analysis

## Objective
To refine the dataset by engineering new features, analyzing relationships among features, and selecting the most informative ones for model training.

---

## Work Summary

- **Removed Unused Features**: Dropped `product ID` and `rotational speed [rpm]` since they are either redundant or less informative.

- **Feature Engineering**:
  - Created a new feature: **Power (W)** using the formula  
    `power = torque × (rotational speed in rad/s)`
  - Added **rotational speed in rad/s** as a derived feature from rpm.

- **Refined Product Type**:
  - Extracted the type (L, M, H) from `product ID` and stored it as a separate feature `type`.
  - **Encoded** the `type` feature numerically for modeling.

- **Selected Final Features**:
  - `air temperature [K]`
  - `process temperature [K]`
  - `torque [Nm]`
  - `tool wear [min]`
  - `type` (encoded)
  - `rotational speed [rad/s]`

- **Performed Correlation Analysis**:
  - Identified strong correlation between:
    - `air temp` and `process temp` (~0.88)
    - `torque` and `power` (~0.98)
    - `power` and `rotational speed` (strong negative)
  - Based on the analysis, **`power` was dropped** to avoid redundancy and potential overfitting.

- **Final Output**:
  - Created and saved a refined CSV file `selected_features.csv` with the final features.

---

## Next Steps
- Begin model training after AI theory revision
