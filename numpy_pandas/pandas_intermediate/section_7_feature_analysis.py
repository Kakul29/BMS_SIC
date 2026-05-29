# USE: Analyzes regional sales totals, platform/genre diversity,
# year range, and correlation between sales columns.
# Run after section_5 (uses vgsales_preprocessed.csv).

import pandas as pd

df = pd.read_csv('vgsales_preprocessed.csv')

sales_columns = ['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']

print("Regional Sales Totals:")
regional_totals = df[sales_columns].sum()
print(regional_totals)
print(f"\nTotal Global Sales: ${df['Global_Sales'].sum():.2f}M")

print("\nPlatform Analysis:")
print(f"  Unique platforms: {df['Platform'].nunique()}")
print(f"  Most common:      {df['Platform'].mode()[0]}")

print("\nGenre Analysis:")
print(f"  Unique genres: {df['Genre'].nunique()}")
print(f"  Most common:   {df['Genre'].mode()[0]}")

print("\nYear Range:")
print(f"  Earliest: {df['Year'].min()}")
print(f"  Latest:   {df['Year'].max()}")
print(f"  Span:     {df['Year'].max() - df['Year'].min()} years")

print("\nCorrelation Matrix:")
correlation_cols = ['Year', 'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']
print(df[correlation_cols].corr())
