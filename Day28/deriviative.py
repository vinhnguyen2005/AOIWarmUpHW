import numpy as np
import matplotlib.pyplot as plt


def numerical_derivative(f, x, h=1e-5):
    return (f(x+h) - f(x)) / h

def plot_function_and_derivative(f, x_range=(-2, 4), title="Đồ thị f(x) và f’(x)"):
    x_vals = np.linspace(x_range[0], x_range[1], 400)
    y_vals = f(x_vals)
    y_derivative_vals = numerical_derivative(f, x_vals)

    plt.figure(figsize=(8, 5))
    plt.plot(x_vals, y_vals, label="f(x)", color='blue')
    plt.plot(x_vals, y_derivative_vals, label="f’(x) (numerical)", color='red', linestyle="--")

    plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
    plt.axvline(0, color='black', linewidth=0.5, linestyle='--')

    plt.xlabel("x")
    plt.ylabel("f(x) & f’(x)")
    plt.title(title)
    plt.legend()
    plt.grid()
    plt.show()
    
def f1(x):
    return x**2 - 3*x + 2

def f2(x):
    return x**3 - 3*x**2 + 4*x - 2

def f3(x):
    return np.exp(x)

def f4(x):
    return np.log(x)

def f5(x):
    return np.sin(x)

def f6(x):
    return np.cos(x)

def f7(x):
    if np.any(np.abs((x - np.pi / 2) % np.pi) < 0.01):
        return np.nan
    return np.tan(x)

# with x >= 0
def f8(x):
    if x < 0:
        return np.nan
    return np.sqrt(x)

plot_function_and_derivative(f1, title="Đồ thị f(x) = x^2 - 3x + 2 và f’(x)")
plot_function_and_derivative(f2, title="Đồ thị f(x) = x^3 - 2x^2 + 4x - 2 và f’(x)")
plot_function_and_derivative(f3, title="Đồ thị f(x) = e^x và f’(x)")
plot_function_and_derivative(f4, x_range=(0.1, 4), title="Đồ thị f(x) = ln(x) và f’(x)")
plot_function_and_derivative(f5, title="Đồ thị f(x) = sin(x) và f’(x)")
plot_function_and_derivative(f6, title="Đồ thị f(x) = cos(x) và f’(x)")
plot_function_and_derivative(f7, x_range=(-1.5, 1.5), title="Đồ thị f(x) = tan(x) và f’(x)")
plot_function_and_derivative(f8, x_range=(0, 4), title="Đồ thị f(x) = x=căn(0,5) và f’(x)")
