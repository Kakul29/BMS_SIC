import pandas as pd
# Student Performance Analytics Report

data = {
    'Name': ['nithin', 'nithya', 'nikhil', 'nishanth', 'nihal'],
    'Subject': ['be', 'msc', 'bca', 'mtech', 'bsc'],
    'Marks': [85.5, 80.5, 95.5, 75.5, 65.5]
}

df = pd.DataFrame(data)

print("Total Students:", len(df))
print("Average Marks:", df['Marks'].mean())
print("Highest Marks:", df['Marks'].max())
print("Lowest Marks:", df['Marks'].min())
print("Standard Deviation:", df['Marks'].std())

above_avg = df[df['Marks'] > df['Marks'].mean()]

print("\nStudents Above Average:")
print(above_avg)