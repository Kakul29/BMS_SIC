import pandas as pd

data = {
    'Name': ['nithin', 'nithya', 'nikhil', 'nishanth', 'nihal'],
    'Subject': ['be', 'msc', 'bca', 'mtech', 'bsc'],
    'Marks': [85.5, 80.5, 95.5, 75.5, 65.5]
}

df = pd.DataFrame(data) 

# Find Average Marks
average = df['Marks'].mean()
print("Average Marks:", average)


