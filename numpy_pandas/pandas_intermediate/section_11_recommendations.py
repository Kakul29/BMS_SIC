# USE: Prints 10 strategic business recommendations derived from the analysis,
# such as which genres, regions, and platforms to target.
# Run after section_5 (uses vgsales_preprocessed.csv).

import pandas as pd

df = pd.read_csv('vgsales_preprocessed.csv')

sales_columns = ['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']
regional_totals = df[sales_columns].sum()
dominant_region = regional_totals.idxmax().replace('_Sales', '')

recommendations = [
    "Focus on Action and Sports genres — they dominate global sales",
    f"Target the {dominant_region} market as the primary region with localized content",
    "Develop for platforms with proven track records (PlayStation, Xbox, Nintendo)",
    "Consider multi-platform releases to maximize reach",
    "Timing: Release games in Q4 to capitalize on holiday sales",
    "Build strong publisher relationships — top publishers have significant market power",
    "Invest in blockbuster titles — top 10 games hold a large market share",
    "Monitor regional preferences — Japan shows different genre trends than NA/EU",
    "Consider mobile and PC platforms for emerging markets",
    "Leverage successful franchises — sequels tend to perform well"
]

print("STRATEGIC RECOMMENDATIONS:")
for i, rec in enumerate(recommendations, 1):
    print(f"\n  {i}. {rec}")
