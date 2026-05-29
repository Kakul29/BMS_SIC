# USE: Loads the vgsales.csv dataset into a DataFrame.
# Place vgsales.csv in the same folder before running this file.

import pandas as pd

df = pd.read_csv('vgsales.csv')

print(f"Data loaded successfully!")
print(f"Dataset contains {len(df)} records")
