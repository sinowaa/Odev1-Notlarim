import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('sandwich.csv')

# Basic information about the dataset
print("=== Basic Dataset Information ===")
print(f"Number of records: {len(df)}")
print("\nData types:")
print(df.dtypes)
print("\nSummary statistics:")
print(df['antCount'].describe())

# Analysis by bread type
print("\n=== Analysis by Bread Type ===")
bread_stats = df.groupby('bread')['antCount'].agg(['mean', 'median', 'count'])
print(bread_stats)

# Analysis by topping
print("\n=== Analysis by Topping ===")
topping_stats = df.groupby('topping')['antCount'].agg(['mean', 'median', 'count'])
print(topping_stats)

# Analysis by butter
print("\n=== Analysis by Butter ===")
butter_stats = df.groupby('butter')['antCount'].agg(['mean', 'median', 'count'])
print(butter_stats)

# Visualization
plt.figure(figsize=(15, 5))

# Boxplot by bread type
plt.subplot(1, 3, 1)
df.boxplot(column='antCount', by='bread', grid=False)
plt.title('Ant Count by Bread Type')
plt.suptitle('')
plt.ylabel('Ant Count')

# Boxplot by topping
plt.subplot(1, 3, 2)
df.boxplot(column='antCount', by='topping', grid=False)
plt.title('Ant Count by Topping')
plt.suptitle('')
plt.ylabel('Ant Count')

# Boxplot by butter
plt.subplot(1, 3, 3)
df.boxplot(column='antCount', by='butter', grid=False)
plt.title('Ant Count by Butter')
plt.suptitle('')
plt.ylabel('Ant Count')

plt.tight_layout()
plt.show()

# Top 5 combinations with highest ant counts
print("\n=== Top 5 Sandwich Combinations by Ant Count ===")
top_combinations = df.sort_values('antCount', ascending=False).head(5)
print(top_combinations[['bread', 'topping', 'butter', 'antCount']])