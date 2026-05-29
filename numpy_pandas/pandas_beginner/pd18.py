# Pie Chart of Marks Distribution

import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Name': ['nithin', 'nithya', 'nikhil', 'nishanth', 'nihal'],
    'Marks': [85.5, 80.5, 95.5, 75.5, 65.5]
}

df = pd.DataFrame(data)

plt.pie(
    df['Marks'],
    labels=df['Name'],
    autopct='%1.1f%%'
)

plt.title("Marks Distribution")

plt.show()
