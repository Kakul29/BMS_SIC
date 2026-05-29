# Grouping data by Age and calculating mean Salary
# Using groupby() to aggregate data and compute mean salary

import pandas as pd

data = {
    'Name': ['nithin', 'nithya', 'nikhil', 'nishanth', 'nihal'],
    'Age': [20, 22, 22, 20, 23],
    'Subject': ['be', 'msc', 'bca', 'mtech', 'bsc'],
    'Marks': [85.5, 80.5, 95.5, 75.5, 65.5]
}

df = pd.DataFrame(data)

grouped = df.groupby('Age')['Salary'].mean() 

# Groups by Age and calculates mean salary
print(grouped)

# select avg(salary) as Avg_Salary from employees group by age;