# USE: Generates and saves two PNG files with 12 charts covering
# top games, platform/genre/publisher sales, trends, regional splits,
# and a correlation heatmap.
# Run after section_5 (uses vgsales_preprocessed.csv).

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('vgsales_preprocessed.csv')
sales_columns = ['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']

# --- Figure 1: 12-panel overview ---
fig = plt.figure(figsize=(20, 24))

# 1. Top 10 Best-Selling Games
ax1 = plt.subplot(4, 3, 1)
top_games = df.nlargest(10, 'Global_Sales')
ax1.barh(range(len(top_games)), top_games['Global_Sales'], color='skyblue')
ax1.set_yticks(range(len(top_games)))
ax1.set_yticklabels(top_games['Name'], fontsize=8)
ax1.set_xlabel('Global Sales (Millions)')
ax1.set_title('Top 10 Best-Selling Video Games', fontweight='bold')
ax1.invert_yaxis()

# 2. Sales by Platform
ax2 = plt.subplot(4, 3, 2)
platform_total = df.groupby('Platform')['Global_Sales'].sum().sort_values(ascending=False).head(10)
ax2.bar(range(len(platform_total)), platform_total.values, color='coral')
ax2.set_xticks(range(len(platform_total)))
ax2.set_xticklabels(platform_total.index, rotation=45, ha='right')
ax2.set_ylabel('Total Sales (Millions)')
ax2.set_title('Top 10 Platforms by Total Sales', fontweight='bold')

# 3. Market Share by Genre (Pie)
ax3 = plt.subplot(4, 3, 3)
genre_total = df.groupby('Genre')['Global_Sales'].sum().sort_values(ascending=False)
colors = plt.cm.Set3(range(len(genre_total)))
ax3.pie(genre_total.values, labels=genre_total.index, autopct='%1.1f%%', colors=colors, startangle=90)
ax3.set_title('Market Share by Genre', fontweight='bold')

# 4. Sales Trends Over Time
ax4 = plt.subplot(4, 3, 4)
yearly = df.groupby('Year')['Global_Sales'].sum()
ax4.plot(yearly.index, yearly.values, marker='o', linewidth=2, color='darkblue')
ax4.fill_between(yearly.index, yearly.values, alpha=0.3)
ax4.set_xlabel('Year')
ax4.set_ylabel('Total Sales (Millions)')
ax4.set_title('Video Game Sales Trends Over Time', fontweight='bold')
ax4.grid(True, alpha=0.3)

# 5. Regional Sales Distribution (Pie)
ax5 = plt.subplot(4, 3, 5)
regional_data = df[sales_columns].sum()
ax5.pie(regional_data.values, labels=regional_data.index, autopct='%1.1f%%', startangle=90)
ax5.set_title('Regional Sales Distribution', fontweight='bold')

# 6. Top 10 Publishers
ax6 = plt.subplot(4, 3, 6)
top_publishers = df.groupby('Publisher')['Global_Sales'].sum().sort_values(ascending=False).head(10)
ax6.barh(range(len(top_publishers)), top_publishers.values, color='lightgreen')
ax6.set_yticks(range(len(top_publishers)))
ax6.set_yticklabels(top_publishers.index, fontsize=8)
ax6.set_xlabel('Total Sales (Millions)')
ax6.set_title('Top 10 Publishers by Total Sales', fontweight='bold')
ax6.invert_yaxis()

# 7. Games Released by Year
ax7 = plt.subplot(4, 3, 7)
games_per_year = df.groupby('Year').size()
ax7.bar(games_per_year.index, games_per_year.values, color='mediumpurple', alpha=0.7)
ax7.set_xlabel('Year')
ax7.set_ylabel('Number of Games Released')
ax7.set_title('Game Releases Over Time', fontweight='bold')

# 8. Average Sales by Genre
ax8 = plt.subplot(4, 3, 8)
avg_genre_sales = df.groupby('Genre')['Global_Sales'].mean().sort_values(ascending=False)
ax8.bar(range(len(avg_genre_sales)), avg_genre_sales.values, color='orange')
ax8.set_xticks(range(len(avg_genre_sales)))
ax8.set_xticklabels(avg_genre_sales.index, rotation=45, ha='right')
ax8.set_ylabel('Average Sales (Millions)')
ax8.set_title('Average Sales by Genre', fontweight='bold')

# 9. Heatmap: Regional Preferences by Genre
ax9 = plt.subplot(4, 3, 9)
genre_regional = df.groupby('Genre')[sales_columns].sum()
sns.heatmap(genre_regional, annot=True, fmt='.1f', cmap='YlOrRd', ax=ax9)
ax9.set_title('Regional Preferences by Genre', fontweight='bold')

# 10. Sales Distribution Box Plot
ax10 = plt.subplot(4, 3, 10)
sales_data = [df['NA_Sales'], df['EU_Sales'], df['JP_Sales'], df['Other_Sales']]
bp = ax10.boxplot(sales_data, labels=['NA', 'EU', 'JP', 'Other'], patch_artist=True)
for patch, color in zip(bp['boxes'], ['lightblue', 'lightgreen', 'lightcoral', 'lightyellow']):
    patch.set_facecolor(color)
ax10.set_ylabel('Sales (Millions)')
ax10.set_ylim(0, 10)
ax10.set_title('Sales Distribution by Region', fontweight='bold')

# 11. Top Platforms by Game Count
ax11 = plt.subplot(4, 3, 11)
platform_count = df['Platform'].value_counts().head(10)
ax11.bar(range(len(platform_count)), platform_count.values, color='steelblue')
ax11.set_xticks(range(len(platform_count)))
ax11.set_xticklabels(platform_count.index, rotation=45, ha='right')
ax11.set_ylabel('Number of Games')
ax11.set_title('Top 10 Platforms by Game Count', fontweight='bold')

# 12. Correlation Heatmap
ax12 = plt.subplot(4, 3, 12)
correlation_cols = ['Year', 'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']
correlation_matrix = df[correlation_cols].corr()
sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm', center=0, square=True, ax=ax12)
ax12.set_title('Sales Correlation Matrix', fontweight='bold')

plt.tight_layout()
plt.savefig('vgsales_analysis_visualizations.png', dpi=300, bbox_inches='tight')
print("Saved: vgsales_analysis_visualizations.png")
plt.show()

# --- Figure 2: 4-panel detailed ---
fig2, axes = plt.subplots(2, 2, figsize=(16, 12))

top_genres = df.groupby('Genre')['Global_Sales'].sum().nlargest(5).index
regional_comparison = df[df['Genre'].isin(top_genres)].groupby('Genre')[sales_columns].sum()
regional_comparison.plot(kind='bar', ax=axes[0, 0], stacked=False)
axes[0, 0].set_title('Regional Sales for Top 5 Genres', fontweight='bold')
axes[0, 0].tick_params(axis='x', rotation=45)

decade_sales = df.groupby('Decade')['Global_Sales'].sum()
axes[0, 1].plot(decade_sales.index, decade_sales.values, marker='D', linewidth=3, markersize=10, color='darkgreen')
axes[0, 1].fill_between(decade_sales.index, decade_sales.values, alpha=0.3, color='lightgreen')
axes[0, 1].set_title('Sales by Decade', fontweight='bold')

success_counts = df['Success_Category'].value_counts()
axes[1, 0].pie(success_counts.values, labels=success_counts.index, autopct='%1.1f%%',
               colors=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99'], startangle=90)
axes[1, 0].set_title('Games by Success Category', fontweight='bold')

top_years = df.groupby('Year')['Global_Sales'].sum().nlargest(15).sort_values(ascending=True)
axes[1, 1].barh(range(len(top_years)), top_years.values, color='crimson')
axes[1, 1].set_yticks(range(len(top_years)))
axes[1, 1].set_yticklabels(top_years.index)
axes[1, 1].set_title('Top 15 Years by Sales', fontweight='bold')

plt.tight_layout()
plt.savefig('vgsales_detailed_analysis.png', dpi=300, bbox_inches='tight')
print("Saved: vgsales_detailed_analysis.png")
plt.show()
