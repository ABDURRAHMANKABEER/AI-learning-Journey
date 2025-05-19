# Tasks
## Day 1
- Read: What is data cleaning?
- Learn: Types of dirty data (missing values, duplicates, wrong formats, etc.)
- Practice: Load sample CSV using pandas
- Task: Identify and list issues in the sample dataset (missing values, typos, etc.)


## Day 2
- Learn: Techniques to handle missing data (dropna, fillna, interpolation)
- Practice: Apply these methods on the dataset
- Task: Document which method you used and why


## Day 3 – Data Cleaning Progress
Focus:

Handling wrong data types

Fixing inconsistent formats and typos

Standardizing text columns

Tasks Completed:

✅ Loaded and reviewed the dirty dataset
✅ Replaced missing values in All Time Peak and Peak with "Unknown"
✅ Identified and corrected column name issues (e.g., fixed 'All Time peak' → 'All Time Peak')
✅ Created a function to clean currency columns (e.g., Actual Gross, Adjusted Gross, Average Gross)
✅ Removed currency symbols ($, ,) and converted values to numeric
✅ Investigated complex formats like "10[2]" in Peak columns and decided to keep or clean based on future use
✅ Standardized text formats in key columns (e.g., .str.lower(), .strip())


## ✅ Day 4 Summary: Data Cleaning Progress
🔧 Tasks Completed:
Standardized Text Columns

Removed special characters, numbers in brackets (e.g. [1]), and inconsistent formatting from string-based columns like song titles and genres.

Applied consistent casing (e.g., .str.title() or .str.lower() where appropriate).

Handled Missing Data in Numeric Columns

Manually filled two missing values using .loc/.iloc for precise control.

Confirmed all missing data is now handled.

Checked for Duplicates

Verified that the dataset contains no duplicate rows using df.duplicated().sum().

Final Touches

Cleaned any irrelevant or malformed symbols.

Exported a final cleaned dataset.