import pandas as pd

data = {
    'Name': ['nithin', 'nithya', 'nikhil', 'nishanth', 'nihal'],
    'Age': [20, 22, 22, 20, 23],
    'Subject': ['be', 'msc', 'bca', 'mtech', 'bsc'],
    'Marks': [85.5, 80.5, 95.5, 75.5, 65.5]
}

df = pd.DataFrame(data)

# Find Student with Highest Marks
topper = df[df['Marks'] == df['Marks'].max()]
print(topper)

# Save DataFrame to CSV File
df.to_csv('students.csv', index=False)
print("File saved successfully")
