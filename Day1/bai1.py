import numpy as np
import random
import matplotlib.pyplot as plt

# Bai 1
def get_thiencan(year):
    thiencan_index = year % 10
    thiencan_list = ["Canh", "Tân", "Nhâm", "Quý", "Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ"]
    return thiencan_list[thiencan_index]

def get_diachi(year):
    diachi_index = year % 12
    diachi_list = ['Thân', 'Dậu', 'Tuất', 'Hợi', 'Tý', 'Sửu', 'Dần', 'Mẹo', 'Thìn', 'Tỵ', 'Ngọ', 'Mùi']
    return diachi_list[diachi_index]

def calculate_can_chi_calendar(year):
    result = ''
    result = get_thiencan(year) + ' ' + get_diachi(year)
    return result

print('2025: ' + calculate_can_chi_calendar(2025))
print('2005: ' + calculate_can_chi_calendar(2005))



#Bai2
def relu(x):
    return np.maximum(x, 0)
print('Relu Function:' + f'{relu(0): .2f}')

def leaked_relu(x, aplha = 0.01):
    return np.maximum(x, aplha * x)
print('Leaked Relu Function:' + f'{leaked_relu(0): .2f}')

def sigmoid(x):
    return 1 / (1 + np.exp(-x))
print('Sigmoid Function:' + f'{sigmoid(2): .2f}')

def tanh(x):
    return (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))
print('Tanh Function:' + f'{tanh(2): .2f}')

def elu(x, alpha=1.0):
    return np.where(x > 0, x, alpha * (np.exp(x) - 1))
print('ELU Function:' + f'{elu(-2): .2f}')