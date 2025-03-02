import numpy as np
import matplotlib . pyplot as plt
import pandas as pd

class LinearRegression:
    def __init__(self, learning_rate=0.01, epochs=1000):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.weights = None
        self.bias = None
        self.costs = []
        
    def predict(self, X):
        return np.dot(X, self.weights) + self.bias
    
    def gradient(self, y_hat, y, X):
        loss = y_hat - y
        dw = np.dot(X.T, loss) / len(y)
        db = np.sum(loss) / len(y)
        cost = np.sum(loss ** 2) / (2*len(y))
        return dw, db, cost
    

    
    def fit(self, X, y):
        self.weights = np.zeros(X.shape[1])
        self.bias = 1
        self.costs = []
        for _ in range(self.epochs):
            y_hat = self.predict(X)
            dw, db, cost = self.gradient(y_hat, y, X)
            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db
            self.costs.append(cost)

    
    def plot_cost(self):
        plt.figure(figsize=(10,6))
        plt.plot(self.costs)
        plt.xlabel('Epoch')
        plt.ylabel('Cost')
        plt.title('Cost vs Epoch')
        plt.grid(True)
        plt.show()
 
data_advertising = pd.read_csv('Day17/advertising (1).csv')
epoch_max = 1000
lr = 0.01   
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_data = data_advertising.drop(['Sales'], axis=1)
Y_data = data_advertising['Sales']

X_data = scaler.fit_transform(X_data)
model = LinearRegression(learning_rate=lr, epochs=epoch_max)
model.fit(X_data, Y_data)
model.plot_cost()