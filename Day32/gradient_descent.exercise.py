import numpy as np

# Ma trận X: USD Index, Lạm phát (%), Giá dầu (USD)
X = np.array([
    [92.5, 2.1, 65.3],
    [93.2, 2.5, 67.2],
    [91.8, 2.3, 64.0],
    [94.0, 2.8, 70.1],
    [95.2, 3.0, 72.5],
    [96.1, 3.2, 74.3],
    [90.5, 1.8, 61.0],
    [92.0, 2.0, 63.2],
    [89.5, 1.5, 59.8],
    [97.0, 3.5, 76.2],
    [95.8, 3.1, 73.8],
    [94.5, 2.9, 71.5],
    [91.2, 2.2, 62.8],
    [90.0, 1.7, 60.5],
    [98.0, 3.7, 78.0],
    [99.2, 4.0, 80.5],
    [88.5, 1.3, 58.0],
    [87.8, 1.1, 56.5],
    [86.5, 1.0, 55.0],
    [100.0, 4.2, 82.0],
])

# Vector y: Giá vàng (USD)
y = np.array([
    1800, 1825, 1795, 1850, 1880, 1905, 1750, 1780, 1725, 1925,
    1890, 1860, 1775, 1740, 1950, 1980, 1700, 1680, 1650, 2000
])

class LinearRegression:
    def __init__(self):
        self.w = np.zeros(X.shape[1])
        self.b = 0
        
    def compute_gradients(self, X, y):
        m = len(y)
        y_pred = X.dot(self.w) + self.b
        error = y_pred - y
        dw = (1/m) * X.T.dot(error)
        db = (1/m) * np.sum(error)
        return dw, db
    
    def fit(self, X , y, learning_Rate=0.001, epochs=10):
        for epoch in range(epochs):
            dw, db = self.compute_gradients(X, y)
            w = self.w - learning_Rate * dw
            b = self.b - learning_Rate * db
            self.w = w
            self.b = b
            loss = 1/ 2*len(y) * np.sum((X.dot(self.w) + self.b - y)**2)
            print(f'Epoch {epoch+1}/{epochs}, Loss: {loss:.4f}')
        
    def predict(self, X):
        return X.dot(self.w) + self.b
    
X_normalized = ( X - np . mean (X , axis =0) ) / np . std (X , axis =0)

model = LinearRegression()
model.fit(X_normalized, y, learning_Rate=0.01, epochs=1000)

print("\nFinal weights:", model.w)
print("Final bias:", model.b)

y_pred = model.predict(X_normalized)
print ("\nSo sánh kết quả thực tế và dự đoán:")
for i in range(5):
    print(f"Thực tế: {y[i]}, Dự đoán: {y_pred[i]:.2f}")