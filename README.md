# DSA4153 Final Project - Group 3 

##Initial Data Inspection

The initial inspection was performed on the four datasets before data cleaning and integration.

The inspection checks:
- Number of rows and columns
- Column names
- Data types
- First five rows
- Missing values
- Completely empty columns
- Duplicate rows
- Date/time columns and date ranges
- Numeric columns

### Initial Findings

#### World Bank Inflation
- 265 rows and 71 columns
- Yearly data from 1960 to 2025
- Contains missing values
- Contains a completely empty `Unnamed: 70` column
- No duplicate rows

#### World Bank Exchange Rate
- 265 rows and 71 columns
- Yearly data from 1960 to 2025
- Contains missing values
- Contains a completely empty `Unnamed: 70` column
- No duplicate rows

#### Geopolitical Events
- 35 rows and 4 columns
- No missing values
- No completely empty columns
- No duplicate rows
- Dates range from 2010 to 2026

#### USD/PHP Historical Data
- 262 rows and 7 columns
- Dates range from October 2025 to October 2026
- `Vol.` is completely empty
- `Date` and `Change %` require type checking/conversion
- No duplicate rows

### Issues Identified

The inspection identified several issues that will need to be addressed during later data preparation:

- Missing values in the World Bank datasets
- Completely empty columns in the World Bank and USD/PHP datasets
- Different data formats and structures
- Different time ranges and data granularities
- Date and numeric fields that may require conversion