import numpy as np

# Bai 1
print("Bài 1:")
x = np.array([2, 4, 6, 8])
p = np.array([0.1, 0.3, 0.4, 0.2])
print(f"E(X) = {np.sum(x*p)}")
# Bai 2
print("Bài 2:")
data = np.random.normal(5, 2, 1000)
mean = np.mean(data)
print(f"E(X) = {mean}")
# Bai 3
print("Bài 3:")
y_pred = np.array([0.1, 0.4, 0.6, 0.9])
y_true = np.array([0, 0, 1, 1])
binary_cross_entropy = (
    -1
    / len(y_true)
    * np.sum(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))
)
print(f"Binary Cross Entropy = {binary_cross_entropy}")
# Bai 4
print("Bài 4:")
rewards = np.random.choice(
    np.arange(0, 11),
    size=100,
    p=[0.05, 0.1, 0.1, 0.15, 0.1, 0.1, 0.1, 0.1, 0.05, 0.1, 0.05],
)
expected_value = np.mean(rewards)
print(f"Giá trị kỳ vọng = {expected_value}")

# Bai 5
print("Bài 5:")
model1 = np.array([[0.2, 0.5, 0.3], [0.1, 0.7, 0.2]])
model2 = np.array([[0.3, 0.4, 0.3], [0.2, 0.6, 0.2]])

labels = np.array([1,1])

def cross_entropy(y_true, y_pred):
    n = len(y_true)
    probabilities = y_pred[np.arange(n), y_true]
    return -np.sum(np.log(probabilities)) / n

binary_cross_entropy_model1 = cross_entropy(labels, model1)
binary_cross_entropy_model2 = cross_entropy(labels, model2)


if binary_cross_entropy_model1 < binary_cross_entropy_model2:
    print("Mô hình 1 tốt hơn với giá trị cross entropy:", binary_cross_entropy_model1)
else:
    print("Mô hình 2 tốt hơn với giá trị cross entropy:", binary_cross_entropy_model2)
