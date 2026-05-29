# Search Student Record System

import pandas as pd

data = {
    'Name': ['nithin', 'nithya', 'nikhil', 'nishanth', 'nihal'],
    'Subject': ['be', 'msc', 'bca', 'mtech', 'bsc'],
    'Marks': [85.5, 80.5, 95.5, 75.5, 65.5]
}

df = pd.DataFrame(data)

student_name = input("Enter student name to search: ")

result = df[df['Name'].str.lower() == student_name.lower()]

if not result.empty:
    print(result)
else:
    print("Student not found")