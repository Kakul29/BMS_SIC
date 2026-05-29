# Line Graph of Student Performance

import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Name': ['nithin', 'nithya', 'nikhil', 'nishanth', 'nihal'],
    'Marks': [85.5, 80.5, 95.5, 75.5, 65.5]
}

df = pd.DataFrame(data)

plt.plot(
    df['Name'],
    df['Marks'],
    marker='o'
)

plt.title("Student Performance Trend")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.grid(True)

plt.show()