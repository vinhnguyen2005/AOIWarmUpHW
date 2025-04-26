import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns   

df = pd.read_csv('Day40/menu.csv')
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())

sns.set(style="whitegrid")

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

sns.histplot(df['Total Fat'], bins=30, kde=False, ax=axes[0], color='skyblue')
axes[0].set_title('Histogram of Total Fat')
axes[0].set_xlabel('Total Fat')
axes[0].set_ylabel('Count')

sns.histplot(df['Total Fat'], bins=30, kde=True, ax=axes[1], color='skyblue', stat='density')
axes[1].set_title('Histogram + KDE of Total Fat')
axes[1].set_xlabel('Total Fat')
axes[1].set_ylabel('Density')

plt.tight_layout()
plt.show()

# Conclusion:
# Cac mon an tap trung trong range tu 0 - 25

correlation = df[['Total Fat', 'Calories']].corr()
plt.figure(figsize=(16, 8))
sns.regplot(x='Total Fat', y='Calories', data=df, color='blue')
plt.title('Total Fat vs Calories')
plt.xlabel('Total Fat')
plt.ylabel('Calories')
plt.show()

# Create joint plot
g = sns.jointplot(
    data=df,
    x='Total Fat',
    y='Calories',
    kind='reg',           
    height=8,             
    marginal_kws=dict(bins=30, fill=True),  
    color='blue'
)

plt.suptitle('Total Fat vs Calories', fontsize=16)
plt.subplots_adjust(top=0.95) 
plt.show()

sns.boxplot(data=df, y='Sodium')
plt.title('Boxplot of Sodium')
plt.ylabel('Sodium')
plt.show()

median = df['Sodium'].median()
q1 = df['Sodium'].quantile(0.25)
q3 = df['Sodium'].quantile(0.75)
iqr = q3 - q1
outliers = df[(df['Sodium'] < (q1 - 1.5 * iqr)) | (df['Sodium'] > (q3 + 1.5 * iqr))]

#remove outliers
df = df[~df.index.isin(outliers.index)]
print("Outliers removed:")
print(outliers)
print("Data after removing outliers:")
print(df)

df.groupby('Category')['Item'].count().plot(kind='bar', color=['skyblue', 'lightgreen', 'salmon', 'orange', 'violet'])
plt.title('Number of Items by Category')
plt.xlabel('Category')
plt.ylabel('Number of Items')
plt.show()
