# USE: Prints a final summary report with dataset overview, market leaders,
# regional breakdown, and performance metrics.
# Run after section_5 (uses vgsales_preprocessed.csv).

import pandas as pd

df = pd.read_csv('vgsales_preprocessed.csv')

sales_columns = ['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']
total_global = df['Global_Sales'].sum()

best_platform       = df.groupby('Platform')['Global_Sales'].sum().idxmax()
best_platform_sales = df.groupby('Platform')['Global_Sales'].sum().max()
best_genre          = df.groupby('Genre')['Global_Sales'].sum().idxmax()
best_genre_sales    = df.groupby('Genre')['Global_Sales'].sum().max()
top_publisher       = df.groupby('Publisher')['Global_Sales'].sum().idxmax()
top_pub_sales       = df.groupby('Publisher')['Global_Sales'].sum().max()
peak_year           = df.groupby('Year')['Global_Sales'].sum().idxmax()
peak_sales          = df.groupby('Year')['Global_Sales'].sum().max()
avg_sales           = df['Global_Sales'].mean()
median_sales        = df['Global_Sales'].median()
top_10_pct          = (df.nlargest(10, 'Global_Sales')['Global_Sales'].sum() / total_global) * 100
platform_count      = df['Platform'].value_counts()

print("=" * 60)
print("ANALYSIS SUMMARY REPORT")
print("=" * 60)

print(f"""
Dataset Overview:
  Total Games Analyzed : {len(df):,}
  Time Period          : {df['Year'].min()} - {df['Year'].max()}
  Total Global Sales   : ${total_global:,.2f} Million
  Platforms Covered    : {df['Platform'].nunique()}
  Genres Covered       : {df['Genre'].nunique()}
  Publishers           : {df['Publisher'].nunique()}

Market Leaders:
  Top Platform  : {best_platform} (${best_platform_sales:.2f}M)
  Top Genre     : {best_genre} (${best_genre_sales:.2f}M)
  Top Publisher : {top_publisher} (${top_pub_sales:.2f}M)
  Peak Year     : {peak_year} (${peak_sales:.2f}M)

Regional Breakdown:
  North America : ${df['NA_Sales'].sum():.2f}M  ({(df['NA_Sales'].sum()/total_global)*100:.1f}%)
  Europe        : ${df['EU_Sales'].sum():.2f}M  ({(df['EU_Sales'].sum()/total_global)*100:.1f}%)
  Japan         : ${df['JP_Sales'].sum():.2f}M  ({(df['JP_Sales'].sum()/total_global)*100:.1f}%)
  Other         : ${df['Other_Sales'].sum():.2f}M  ({(df['Other_Sales'].sum()/total_global)*100:.1f}%)

Performance Metrics:
  Average Game Sales        : ${avg_sales:.2f}M
  Median Game Sales         : ${median_sales:.2f}M
  Top 10 Games Market Share : {top_10_pct:.2f}%
  Most Active Platform      : {platform_count.index[0]} ({platform_count.values[0]} games)
""")

print("=" * 60)
print("ANALYSIS COMPLETED SUCCESSFULLY!")
print("=" * 60)
