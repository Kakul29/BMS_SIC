# Categorize Students into Performance Groups

import pandas as pd

data = {
    'Name': ['nithin', 'nithya', 'nikhil', 'nishanth', 'nihal'],
    'Subject': ['be', 'msc', 'bca', 'mtech', 'bsc'],
    'Marks': [85.5, 80.5, 95.5, 75.5, 65.5]
}

df = pd.DataFrame(data)

conditions = [
    (df['Marks'] >= 90),
    (df['Marks'] >= 75) & (df['Marks'] < 90),
    (df['Marks'] < 75)
]

categories = ['Excellent', 'Good', 'Needs Improvement']

df['Performance'] = pd.Series(index=df.index)

df.loc[conditions[0], 'Performance'] = categories[0]
df.loc[conditions[1], 'Performance'] = categories[1]
df.loc[conditions[2], 'Performance'] = categories[2]

print(df)
