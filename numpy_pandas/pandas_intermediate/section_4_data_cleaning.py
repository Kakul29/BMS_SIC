# USE: Cleans the dataset by handling missing values and removing duplicates.
# Fills missing Year values with the median and missing Publisher with 'Unknown'.

import pandas as pd

df = pd.read_csv('vgsales.csv')
original_shape = df.shape

print("Missing Values:")
print(df.isnull().sum()[df.isnull().sum() > 0])

# Fill missing Year with median
if df['Year'].isnull().sum() > 0:
    median_year = df['Year'].median()
    df['Year'].fillna(median_year, inplace=True)
    print(f"\nFilled missing Year values with median: {median_year}")

# Fill missing Publisher with 'Unknown'
if df['Publisher'].isnull().sum() > 0:
    df['Publisher'].fillna('Unknown', inplace=True)
    print("Filled missing Publisher values with 'Unknown'")

# Remove duplicates
duplicates = df.duplicated().sum()
if duplicates > 0:
    df.drop_duplicates(inplace=True)
    print(f"Removed {duplicates} duplicate records")

# Convert Year to integer
df['Year'] = df['Year'].astype(int)

print(f"\nOriginal shape: {original_shape}")
print(f"Cleaned shape:  {df.shape}")
print(f"Records removed: {original_shape[0] - df.shape[0]}")

# Save cleaned data for use in later sections
df.to_csv('vgsales_cleaned.csv', index=False)
print("\nCleaned data saved as vgsales_cleaned.csv")
