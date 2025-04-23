import numpy as np

# Bai 1
print("Bài 1:")
x = np.array([1,3,5])
P = np.array([0.2,0.5,0.3])
mean = np.sum(x * P)
variance = np.sum(P * (x - mean) ** 2)
print(f"Giá trị kỳ vọng E(X) = {mean}")
print(f"Phương sai Var(X) = {variance}")

#Bai 2
print("Bài 2:")
data = np.random.normal(0, 2, 1000)
population_variance = np.var(data)
sample_variance = np.var(data, ddof=1)
print(f"Phương sai mẫu = {sample_variance}")
print(f"Phương sai tổng thể = {population_variance}")

# Bai 3
print("Bài 3:")
model_a_scores = np . array ([0.8 , 0.7 , 0.9 , 0.75 , 0.85])
model_b_scores = np . array ([0.6 , 0.4 , 0.9 , 0.3 , 0.8])

def calculate_variance(scores):
    return np.var(scores)

model_a_variance = calculate_variance(model_a_scores)
model_b_variance = calculate_variance(model_b_scores)

if model_a_variance < model_b_variance:
    print("Mô hình A ổn định hơn với phương sai:", model_a_variance)
else:
    print("Mô hình B ổn định hơn với phương sai:", model_b_variance)
    
# Bai 4
print("Bài 4:")
pixel_means = np . array ([122 , 120 , 119 , 123 , 121])

pixel_variance = np.var(pixel_means, ddof=1)
print(f"Phương sai pixel của ảnh = {pixel_variance}")

# Bai 5
print("Bài 5:")
rewards = np . array ([10 , 9 , 8 , 10 , 7, 6 , 9 , 10 , 5, 8])
reward_variance = np.var(rewards, ddof=1)
print(f"Phương sai phần thưởng = {reward_variance}")
