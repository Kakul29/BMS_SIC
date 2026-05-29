# USE: Prints detailed sales statistics, regional market share percentages,
# top 5 games by sales, and market concentration metrics.
# Run after section_5 (uses vgsales_preprocessed.csv).

import pandas as pd

df = pd.read_csv('vgsales_preprocessed.csv')

sales_columns = ['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']
total_global = df['Global_Sales'].sum()

print("Sales Statistics:")
print(df[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']].describe())

print("\nRegional Market Share:")
for region in sales_columns:
    region_total = df[region].sum()
    pct = (region_total / total_global) * 100
    print(f"  {region.replace('_Sales', '')}: ${region_total:.2f}M  ({pct:.2f}%)")

print("\nTop 5 Games by Global Sales:")
print(df.nlargest(5, 'Global_Sales')[['Name', 'Platform', 'Year', 'Genre', 'Global_Sales']])

top_10_pct = (df.nlargest(10, 'Global_Sales')['Global_Sales'].sum() / total_global) * 100
print(f"\nTop 10 games account for {top_10_pct:.2f}% of total global sales")
