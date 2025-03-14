import numpy as np
import matplotlib.pyplot as plt
def numerical_derivative (f, x, h=1e-5):
  return (f(x + h) - f(x)) /h

def plot_chain_rule (f, g, x_range=(0, 0), y_range = (0, 0), title="Đạo hàm Chain Rule"):
  x_vals = np.linspace(x_range [0], x_range [1], 400)


  g_vals = g(x_vals)
  f_vals = f(g_vals)

  chain_rule_derivative_vals = numerical_derivative(f, g(x_vals)) * numerical_derivative(g, x_vals)


  plt.figure(figsize=(8,5))
  plt.plot(x_vals, f_vals, label="f(g(x))", color='blue')
  plt.plot(x_vals, chain_rule_derivative_vals, label="f'(x) theo ChainRule", color='red', linestyle="--")
  plt.axhline (0, color='black', linewidth=0.5, linestyle='')
  plt.axvline (0, color='black', linewidth=0.5, linestyle='--')

  plt.xlabel("x")
  plt.ylabel("Giá trị")
  plt.title(title)
  plt.legend()
  plt.grid()

plot_chain_rule(lambda x: np.exp(x), lambda x: x**3 - 2*x + 1, x_range=(-2, 2), y_range = (0, 1400), title = "Bài 1: f(x) = e^(x^3 - 2x + 1)")
plot_chain_rule(lambda x: np.log(x), lambda x: 5*(x**2) + 3*x + 1, x_range=(-1, 2), y_range = (-3, 3), title = "Bài 2: f(x) = ln(5x^2 + 3x + 1)")
plot_chain_rule(lambda x: np.sqrt(x), lambda x: x**4 + 2*(x**2) + 1, x_range=(-2, 2), y_range = (-4, 4), title = "Bài 3: f(x) = sqrt(x^4 + 2x^2 + 1)")
plot_chain_rule(lambda x: np.sin(x), lambda x: x**2 - 3*x + 2, x_range=(-2, 3), y_range = (-6, 6), title = "Bài 4: f(x) = sin(x^2 - 3x + 2)")
plot_chain_rule(lambda x: x**2 + 4, lambda x: x, x_range=(0, 3), y_range = (0, 12), title = "Bài 5: f(x) = e^(ln(x^2 + 4))")
plot_chain_rule(lambda x: x**(-0.5), lambda x: x**3 + x + 2, x_range=(-1, 2), y_range = (-300, 0), title = "Bài 6: f(x) = 1/sqrt(x^3 + x + 2)")
plot_chain_rule(lambda x: np.cos(x), lambda x: np.log(x**2 + 1), x_range=(-2, 2), y_range = (-0.75, 1), title = "Bài 7: f(x) = cos(ln(x^2 + 1))")
plot_chain_rule(lambda x: x**6, lambda x: 3*(x**2) + 5*x + 1, x_range=(-2, 2), y_range = (0, 6), title = "Bài 8: f(x) = (3x^2 + 5x = 1)^6")
plt.show()