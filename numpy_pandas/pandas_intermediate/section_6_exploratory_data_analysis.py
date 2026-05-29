# USE: Explores sales patterns grouped by Platform, Genre, Publisher, and Year.
# Run after section_5 (uses vgsales_preprocessed.csv).

import pandas as pd

df = pd.read_csv('vgsales_preprocessed.csv')

print("Sales by Platform (Top 10):")
platform_sales = df.groupby('Platform')['Global_Sales'].agg(['sum', 'mean', 'count']).sort_values('sum', ascending=False).head(10)
print(platform_sales)

'''
print("\nSales by Genre:")
genre_sales = df.groupby('Genre')['Global_Sales'].agg(['sum', 'mean', 'count']).sort_values('sum', ascending=False)
print(genre_sales)

print("\nSales by Publisher (Top 10):")
publisher_sales = df.groupby('Publisher')['Global_Sales'].agg(['sum', 'mean', 'count']).sort_values('sum', ascending=False).head(10)
print(publisher_sales)

print("\nYearly Sales Trend (Last 10 years in dataset):")
yearly_sales = df.groupby('Year')['Global_Sales'].sum().sort_index()
print(yearly_sales.tail(10))
'''