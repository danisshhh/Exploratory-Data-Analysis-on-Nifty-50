# Exploratory Data Analysis on Nifty 50

This project performs comprehensive exploratory data analysis (EDA) on Nifty 50 stock market data. It includes data cleaning and summary statistics generation to derive insights from the dataset.

## Overview

The Nifty 50 is a benchmark stock market index comprising 50 companies listed on the National Stock Exchange (NSE) of India. This analysis pipeline processes raw stock market data to generate cleaned datasets and statistical summaries.

## Project Structure

```
├── Data_Cleaning.py
├── Summary_Statistics.py
├── nifty50_dataset.csv
└── README.md
```

## Files Description

### `Data_Cleaning.py`
Handles all data preprocessing and cleaning operations:
- **Dataset Loading**: Imports raw Nifty 50 data from CSV
- **Data Inspection**: Displays first rows, data types, and initial statistics
- **Missing Values Handling**: Removes rows with missing values (alternative: forward fill)
- **Duplicate Removal**: Eliminates duplicate records
- **Data Type Conversion**: Converts Date to datetime and numerical columns (Open, High, Low, Close, Volume) to numeric format
- **Outlier Detection**: Uses Interquartile Range (IQR) method to identify and remove outliers
- **Column Standardization**: Normalizes column names to lowercase with underscores
- **Data Filtering**: Retains data from 2020 onwards
- **Output**: Saves cleaned dataset as `cleaned_nifty50_dataset.csv`

### `Summary_Statistics.py`
Generates statistical summaries of the dataset:
- **Data Loading**: Reads the Nifty 50 CSV file
- **Data Type Conversion**: Ensures proper formatting of Date and numerical columns
- **Summary Statistics**: Computes and displays descriptive statistics (count, mean, std, min, max, quartiles) for all numerical columns

### `nifty50_dataset.csv`
Raw input dataset containing Nifty 50 stock market data with columns:
- Date
- Open
- High
- Low
- Close
- Volume

## Requirements

- Python 3.x
- pandas

## Installation

Install required packages:
```bash
pip install pandas
```

## Usage

### Step 1: Data Cleaning
Run the data cleaning script to preprocess the raw data:
```bash
python Data_Cleaning.py
```

This will:
- Clean and validate the dataset
- Handle missing values and outliers
- Output a cleaned CSV file

### Step 2: Generate Summary Statistics
Run the summary statistics script:
```bash
python Summary_Statistics.py
```

This will display:
- Statistical measures (mean, median, standard deviation, etc.)
- Data distribution information for all numerical columns

## Data Processing Pipeline

```
Raw Data (nifty50_dataset.csv)
        ↓
  Data Cleaning
        ↓
- Remove missing values
- Remove duplicates
- Convert data types
- Detect & remove outliers
- Standardize column names
- Filter by date range
        ↓
Cleaned Data (cleaned_nifty50_dataset.csv)
        ↓
  Summary Statistics
        ↓
Statistical Insights
```

## Key Features

✓ Comprehensive data validation and cleaning  
✓ Outlier detection using IQR method  
✓ Automatic data type conversion  
✓ Duplicate removal  
✓ Temporal filtering (2020 onwards)  
✓ Descriptive statistical analysis  

## Notes

- Update file paths in both scripts if the dataset location changes
- The IQR method removes records with outliers in any numerical column
- Summary statistics are computed only on remaining data after cleaning
- Column names are standardized to snake_case format after cleaning

## Future Enhancements

- Visualization of trends and distributions
- Correlation analysis between stock metrics
- Time-series analysis and forecasting
- Sector-wise analysis
- Performance metrics and KPIs
