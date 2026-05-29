# USE: Creates new features (Decade, Dominant_Region, Success_Category)
# and encodes categorical columns for analysis.
# Run after section_4 (uses vgsales_cleaned.csv).

import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('vgsales_cleaned.csv')

sales_columns = ['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']

# New features
df['Decade'] = (df['Year'] // 10) * 10
df['Dominant_Region'] = df[sales_columns].idxmax(axis=1).str.replace('_Sales', '')
df['Success_Category'] = pd.cut(
    df['Global_Sales'],
    bins=[0, 1, 5, 10, float('inf')],
    labels=['Low', 'Medium', 'High', 'Blockbuster']
)

print("New features created: Decade, Dominant_Region, Success_Category")

# Encode categorical columns
le = LabelEncoder()
df['Platform_Encoded'] = le.fit_transform(df['Platform'])
df['Genre_Encoded']    = le.fit_transform(df['Genre'])
df['Publisher_Encoded'] = le.fit_transform(df['Publisher'])

print("Categorical columns encoded: Platform, Genre, Publisher")

# Save preprocessed data
df.to_csv('vgsales_preprocessed.csv', index=False)
print("Preprocessed data saved as vgsales_preprocessed.csv")
