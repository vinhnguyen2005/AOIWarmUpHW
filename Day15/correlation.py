import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv("Day15/advertising (1).csv", encoding="utf-8")
print(data.head(5))
print(data.tail(5))
print(data.info())

def correlation(x, y):
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    numerator = np.sum((x - x_mean) * (y - y_mean))
    denominator = np.sqrt(np.sum((x - x_mean) ** 2)) * np.sqrt(np.sum((y - y_mean) ** 2))
    return numerator / denominator

features = ['TV', 'Radio', 'Newspaper']
for i in features:
    for j in features:
        print(f"Correlation between {i} and {j}: {correlation(data[i], data[j])}")
    
correlation_matrix = data.corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title("Heatmap thể hiện sự tương quan giữa các biến")
plt.show()