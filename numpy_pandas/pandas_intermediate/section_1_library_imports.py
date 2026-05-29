# USE: Run this file first before any other section.
# It imports all required libraries and sets the visualization style.

import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings('ignore')

plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

print("=" * 60)
print("BOOK SALES DATA ANALYSIS PROJECT")
print("=" * 60)
print("All libraries imported successfully.")
