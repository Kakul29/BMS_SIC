# Bar Chart Visualization of Student Marks

import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Name': ['nithin', 'nithya', 'nikhil', 'nishanth', 'nihal'],
    'Marks': [85.5, 80.5, 95.5, 75.5, 65.5]
}

df = pd.DataFrame(data)

plt.bar(df['Name'], df['Marks'])

plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.show()
