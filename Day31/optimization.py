import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**4 - 3*x**3 + 2

def f_prime(x):
    return 4*x**3 - 9 * x ** 2

def gradient_descent(f_prime, x_init, learning_Rate=0.01, epochs=100):
    x = x_init
    history = [x]
    for _ in range(epochs):
        x = x - learning_Rate * f_prime(x)
        history.append(x)
    return x, history

x_init = 0.5
learning_rate = 0.01
epochs = 100
x_optimal, history = gradient_descent(f_prime, x_init, learning_rate, epochs)

x_vals = np.linspace(-1, 3, 100)
y_vals = f(x_vals)

plt.plot(x_vals, y_vals, label="f(x)")
plt.scatter(history, [f(x) for x in history], color="red", s=10, label="Iterations")
plt.scatter(x_optimal, f(x_optimal), color="green", marker="x", s=100, label=f"Min at x={x_optimal:.3f}")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid()
plt.show()

# Linear Regression
X = np.array([1, 2, 3, 4, 5])
y = np.array([2, 3, 4, 5, 6])

w, b = 0.0, 0.0
learning_rate = 0.01
epochs = 1000

for _ in range(epochs):
    y_pred = w * X + b
    dw = 2 * np.sum((y_pred - y) * X) / len(X)
    db = 2 * np.sum(y_pred - y) / len(X)
    w -= learning_rate * dw
    b -= learning_rate * db

y_pred = w * X + b  

plt.scatter(X, y, label="Data") 
plt.plot(X, y_pred, color='red', label="Regression Line") 
plt.xlabel("X")
plt.ylabel("y")
plt.legend()
plt.grid()
plt.show()

print(f"Hệ số tối ưu: w = {w:.3f}, b = {b:.3f}")

#Newton
#f(x) = x3 − 6x2 + 4x + 12
def f_prime(x):
    return 3*x**2 - 12*x + 4

def f_double_prime(x):
    return 6*x - 12

x = 5
for _ in range(10):
    x = x - f_prime(x) / f_double_prime(x)
    
print ( f"Cực tiểu tại x = {x:.3}")