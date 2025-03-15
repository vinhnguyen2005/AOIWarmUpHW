import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return sigmoid(x) * (1 - sigmoid(x))

x = np.array([ -2 , -1 , 0 , 1 , 2])
print (" Sigmoid :", sigmoid ( x ) )
print (" Sigmoid derivative :", sigmoid_derivative ( x ) )

def mse_derivative(y_true, y_pred):
    return -2 * (y_true - y_pred) / len(y_true)

y_true = np . array ([3 , 5 , 2 , 8])
y_pred = np . array ([2.5 , 4.8 , 2.1 , 7.5])
print (" MSE derivative :", mse_derivative ( y_true , y_pred ) )

def relu(x):
    return np.maximum(0, x)

def relu_derivative(x):
    return np.where(x > 0, 1, 0)

x = np . array ([ -2 , -1 , 0 , 1 , 2])
print (" ReLU :", relu ( x ) )
print (" ReLU derivative :", relu_derivative ( x ) )

def softmax ( z ) :
    return np.exp ( z ) / np.sum ( np.exp ( z ) )

def softmax_derivative ( z ) :
    return softmax ( z ) * (1 - softmax ( z ) )

z = np . array ([2.0 , 1.0 , 0.1])
print (" Softmax :", softmax ( z ) )
print (" Softmax derivative :", softmax_derivative ( z ) )

def tanh(x):
    return np.exp(x) - np.exp(-x) / np.exp(x) + np.exp(-x)

def tanh_derivative(x):
    return 1 - tanh(x)**2

x = np . array ([ -2 , -1 , 0 , 1 , 2])
print (" Tanh :", tanh ( x ) )
print (" Tanh derivative :", tanh_derivative ( x ) )