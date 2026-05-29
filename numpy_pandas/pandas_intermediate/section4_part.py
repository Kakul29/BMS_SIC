import pandas as pd

df = pd.read_csv('vgsales.csv')
original_shape = df.shape

print("Missing Values:")
print(df.isnull().sum()[df.isnull().sum() > 0])