import pandas as pd
# Grade Classification System

data = {
    'Name': ['nithin', 'nithya', 'nikhil', 'nishanth', 'nihal'],
    'Subject': ['be', 'msc', 'bca', 'mtech', 'bsc'],
    'Marks': [85.5, 80.5, 95.5, 75.5, 65.5]
}

df = pd.DataFrame(data)

def calculate_grade(mark):
    if mark >= 90:
        return 'A+'
    elif mark >= 80:
        return 'A'
    elif mark >= 70:
        return 'B'
    elif mark >= 60:
        return 'C'
    else:
        return 'Fail'

df['Grade'] = df['Marks'].apply(calculate_grade)

print(df)