import numpy as np
# Cong tru ma tran

def sum_matrix(A, B):
    return np.add(A, B)

def subtract_matrix(A, B):
    return np.subtract(A, B)

def hadamard_matrix(A, B):
    return np.multiply(A, B)

def dot_product(v1, v2):
    return np.dot(v1, v2)

def convolution(matrix, kernel):
    rows = matrix.shape[0] - kernel.shape[0] + 1
    cols = matrix.shape[1] - kernel.shape[1] + 1
    res = np.zeros((rows, cols))
    for i in range(rows):
        for j in range(cols):
            sum = 0
            for k in range(kernel.shape[0]):
                for l in range(kernel.shape[1]):
                    sum += matrix[i + k][j + l] * kernel[k][l]
            res[i, j] = sum
        
    return res


def rotate(v, degree):
    R = np.array([[np.cos(degree), -np.sin(degree)],
                  [np.sin(degree), np.cos(degree)]])
    return v.dot(R)

#Bai Toan 1:
matrix_a = np.array([
    [1, 2],
    [3, 4]
])

matrix_b = np.array([
    [5, 6],
    [7, 8]
])


print(f"Sum : \n {sum_matrix(matrix_a, matrix_b)}")
print(f"Minus : \n {subtract_matrix(matrix_a, matrix_b)}")

#Hadamard
matrix_a = np.array([
    [1, 2],
    [3, 4]
])

matrix_b = np.array([
    [5, 6],
    [7, 8]
])

print(f"Hadamard : \n {hadamard_matrix(matrix_a, matrix_b)}")

vec_a = np.array([1, 2, 3])
vec_b = np.array([4, 5, 6])
print(f"Dot product : {dot_product(vec_a, vec_b)}")

matrix_a = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

kernel = np.array([
    [1, 0],
    [0, -1]
])

print(f"Convolution result:\n{convolution(matrix_a, kernel)}")

v = np.array([1, 0])
degree = 45
print(f"Rotation matrix:\n{rotate(v, degree)}")


