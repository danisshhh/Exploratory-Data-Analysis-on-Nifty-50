import pandas as pd

# Step 1: Load the dataset
file_path = "/mnt/data/nifty50_dataset.csv"
df = pd.read_csv(file_path)

# Step 2: Inspect the Dataset
print(df.head())
print(df.info())
print(df.describe())

# Step 3: Handle Missing Values
# Option 1: Drop rows with missing values
df = df.dropna()

# Option 2: Fill missing values (e.g., forward fill)
# df = df.fillna(method='ffill')

# Step 4: Remove Duplicates
df = df.drop_duplicates()

# Step 5: Data Type Conversion
# Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Ensure numerical columns are in the correct format
numerical_columns = ['Open', 'High', 'Low', 'Close', 'Volume']
for col in numerical_columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Step 6: Outlier Detection
# Detect outliers using IQR to detect outliers
Q1 = df[numerical_columns].quantile(0.25)
Q3 = df[numerical_columns].quantile(0.75)
IQR = Q3 - Q1
outliers = ((df[numerical_columns] < (Q1 - 1.5 * IQR)) | (df[numerical_columns] > (Q3 + 1.5 * IQR)))
df = df[~outliers.any(axis=1)]

# Step 7: Standardize Column Names
df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]

# Step 8: Filter Data
# Assuming we want to keep data only from 2020 onwards
df = df[df['date'] >= '2020-01-01']

# Save the cleaned dataset
cleaned_file_path = "/mnt/data/cleaned_nifty50_dataset.csv"
df.to_csv(cleaned_file_path, index=False)

print("Data cleaning complete. Cleaned data saved to", cleaned_file_path)
