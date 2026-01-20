import pandas as pd

# Step 1: Load the dataset
file_path = "nifty50_dataset.csv"  # Adjust the path as needed
df = pd.read_csv(file_path)

# Step 2: Data Type Conversion
# Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Ensure numerical columns are in the correct format
numerical_columns = ['Open', 'High', 'Low', 'Close', 'Volume']
for col in numerical_columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Step 3: Generate Summary Statistics
summary_statistics = df.describe()

# Display the summary statistics
print(summary_statistics)
