import pandas as pd
# Load the CSV file into a DataFrame
df = pd.read_csv("sample_data.csv")
# Display the first few rows of the DataFrame
print("Data Preview:")
print(df.head())
# Get a summary of the DataFrame, including data types
print("\nDataFrame Info:")
print(df.info())
# Basic filtering: find rows where Age > 30
filtered_df = df[df["Age"] > 30]
print("\nRows where Age > 30:")
print(filtered_df)
# Compute summary statistics for numeric columns
print("\nSummary Statistics:")
print(df.describe())