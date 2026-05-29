# USE: Automatically generates 8 key business insights from the dataset,
# such as best platform, top genre, peak year, and dominant region.
# Run after section_5 (uses vgsales_preprocessed.csv).

import pandas as pd

df = pd.read_csv('vgsales_preprocessed.csv')

sales_columns = ['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']
regional_totals = df[sales_columns].sum()
total_global = df['Global_Sales'].sum()

insights = []

best_platform       = df.groupby('Platform')['Global_Sales'].sum().idxmax()
best_platform_sales = df.groupby('Platform')['Global_Sales'].sum().max()
insights.append(f"1. {best_platform} is the best-selling platform with ${best_platform_sales:.2f}M in total sales")

best_genre       = df.groupby('Genre')['Global_Sales'].sum().idxmax()
best_genre_sales = df.groupby('Genre')['Global_Sales'].sum().max()
insights.append(f"2. {best_genre} is the top-selling genre with ${best_genre_sales:.2f}M in total sales")

peak_year  = df.groupby('Year')['Global_Sales'].sum().idxmax()
peak_sales = df.groupby('Year')['Global_Sales'].sum().max()
insights.append(f"3. {peak_year} was the peak year with ${peak_sales:.2f}M in total sales")

dominant_region = regional_totals.idxmax().replace('_Sales', '')
insights.append(f"4. {dominant_region} is the dominant market ({(regional_totals.max()/total_global)*100:.1f}% of global sales)")

top_publisher      = df.groupby('Publisher')['Global_Sales'].sum().idxmax()
top_pub_sales      = df.groupby('Publisher')['Global_Sales'].sum().max()
insights.append(f"5. {top_publisher} leads publishers with ${top_pub_sales:.2f}M in total sales")

avg_sales    = df['Global_Sales'].mean()
median_sales = df['Global_Sales'].median()
insights.append(f"6. Average game sales: ${avg_sales:.2f}M, Median: ${median_sales:.2f}M")

insights.append(f"7. Dataset covers {df['Year'].max() - df['Year'].min()} years ({df['Year'].min()}-{df['Year'].max()})")
insights.append(f"8. Market has {df['Genre'].nunique()} genres across {df['Platform'].nunique()} platforms")

print("KEY INSIGHTS:")
for insight in insights:
    print(f"\n  {insight}")
