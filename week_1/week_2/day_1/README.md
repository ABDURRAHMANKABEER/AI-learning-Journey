# 📅 Day 1 — Exploratory Data Analysis (EDA) & Dataset Understanding
🔍 Objective
To understand the structure, distribution, and integrity of the AI4I 2020 Predictive Maintenance Dataset, identify data types, spot anomalies or patterns, and prepare the dataset for modeling.

**📌 Activities Completed**
Dataset Loaded

Successfully imported the dataset using pandas.

Observed 10,000 rows and 14 columns including sensor readings and failure labels.

Basic Inspection

Used .info() and .describe() to view data types, null values, and statistical summaries.

Verified that the machine failure target is heavily imbalanced with mostly 0s (normal operation).

Feature Categorization

Identified 6 primary sensor-based numerical features:

Air temperature [K], Process temperature [K], Rotational speed [rpm], Torque [Nm], Tool wear [min], and Product ID (later removed).

The remaining 6 are binary failure labels (including machine failure as the target).

Visualization: Histograms & Boxplots

Created histograms and boxplots for each numerical feature.

Observed that most distributions are slightly skewed, but no extreme outliers were detected based on frequency behavior and proximity of values.

Detected that some high-frequency values that seemed like outliers actually belonged to natural operational zones.

Initial Insights

Understood that machine failure is a composite label derived from 5 different failure types.

Noted that some of these failure conditions depend directly on sensor thresholds (e.g., torque × tool wear for OSF).

Determined that Product ID contains encoded information and may not be needed for predictive modeling.

**✅ Skills Practiced**
Data inspection and summary

Visualization using matplotlib and seaborn

Feature interpretation and dataset exploration

Critical thinking around feature-target relationships

**📁 Output Artifacts**
01_data_cleaning_and_eda.ipynb: Notebook documenting the cleaning and exploration

Initial cleaned dataset ready for feature correlation and deeper analysis