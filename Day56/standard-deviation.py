import numpy as np

# Bai 1
print("Bài 1:")
x = np.array([2, 4, 6])
p = np.array([0.3, 0.4, 0.3])
mean = np.sum(x * p)
std = np.sqrt(np.sum(p * (x - mean) ** 2))
print(f"Giá trị kỳ vọng E(X) = {mean}")
print(f"Độ lệch chuẩn = {std}")

# Bai 2
print("Bài 2:")
data = np.random.normal(10, 3, 1000)
population_std = np.std(data)
sample_std = np.std(data, ddof=1)
print(f"Độ lệch chuẩn mẫu = {sample_std}")
print(f"Độ lệch chuẩn tổng thể = {population_std}")

# Bai 3
print("Bài 3:")
model_a_scores = np.array([0.85, 0.86, 0.84, 0.87])
model_b_scores = np.array([0.9, 0.6, 0.95, 0.5])


def calculate_std(scores):
    return np.std(scores)


model_a_std = calculate_std(model_a_scores)
model_b_std = calculate_std(model_b_scores)
if model_a_std < model_b_std:
    print("Mô hình A ổn định hơn với độ lệch chuẩn:", model_a_std)
else:
    print("Mô hình B ổn định hơn với độ lệch chuẩn:", model_b_std)

# Bai 4
print("Bài 4:")
pixel_values = np.array([123, 124, 122, 121, 125, 123, 124, 122, 120, 123])
pixel_std = np.std(pixel_values, ddof=1)
print(f"Độ lệch chuẩn pixel của ảnh = {pixel_std}")

# Bai 5
print("Bài 5:")
rewards = np.array([8, 7, 8, 9, 7, 8, 9, 8, 7, 8, 6, 8, 7, 8, 8, 7, 8, 9, 7, 8])
std = np.std(rewards, ddof=1)
if std < 1:
    print("Phần thưởng ổn định với độ lệch chuẩn:", std)
else:
    print("Phần thưởng không ổn định với độ lệch chuẩn:", std)