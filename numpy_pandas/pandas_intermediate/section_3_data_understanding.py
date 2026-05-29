# USE: Gives a first look at the dataset — shape, column types,
# sample rows, and basic statistics. Run after section_2.

import pandas as pd

df = pd.read_csv('vgsales.csv')

print("Dataset Shape:", df.shape[0], "rows x", df.shape[1], "columns")

print("\nColumn Info:")
print(df.info())

print("\nFirst 10 Records:")
print(df.head(10))

print("\nDataset Statistics:")
print(df.describe()) #

print("\nColumn Names and Data Types:")
for col in df.columns:
    print(f"  {col}: {df[col].dtype}")
