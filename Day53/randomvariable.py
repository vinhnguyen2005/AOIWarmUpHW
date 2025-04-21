# Bai 1
import numpy as np

print("Bài 1:")
# Sinh ngẫu nhiên 1000 nhãn (labels): 'cat', 'dog', hoặc 'rabbit'
labels = np.random.choice(['cat', 'dog', 'rabbit'], size=1000, p=[0.4, 0.4, 0.2])
print(labels[:10])

# Đếm số lượng từng nhãn
unique, counts = np.unique(labels, return_counts=True)
frequency = dict(zip(unique, counts))

for key, value in frequency.items():
    print(f"{key}: {value}")

# Bai 2 
print("Bài 2:")
vector = np.random.normal(loc=0, scale=1, size=(100, 10))

mean = np.mean(vector)
std = np.std(vector)

print(f"Mean: {mean}")
print(f"Standard Deviation: {std}")

# Bai 3
#Mô phỏng 10.000 điểm từ phân phối chuẩn N (0, 1) và ước lượng xác suất P(−1 <
#X < 1).
print("Bài 3:")
from scipy.stats import norm
import matplotlib.pyplot as plt

x = np.random.normal(loc=0, scale=1, size=10000)

probability = np.mean((x > -1) & (x < 1))

print(f"Xác suất P(-1 < X < 1): {probability}")

# Bai 4
print("Bài 4:")

labels = np.random.choice(['positive', 'neutral', 'negative'], size=1000, p=[0.3, 0.5, 0.2])
unique, counts = np.unique(labels, return_counts=True)
pmf = counts / len(labels)

print("PMF:")
for label, count in zip(unique, pmf):
    print(f"{label}: {count}")

# Bai 5
print("Bài 5:")
mu = np.zeros(10)
sigma = np.ones(10)
epsilon = np.random.normal(size=10)

z = mu + sigma * epsilon
print(z)


