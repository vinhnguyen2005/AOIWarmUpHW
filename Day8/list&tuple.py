import math 
import re
import numpy as np
#Cau 1
my_tuple1 = (2, 3)
my_tuple2 = (3, 6)

print('Cau 1:')
print('Vector 1:', my_tuple1)
print('Vector 2:', my_tuple2)

#Cau 2
print('Cau 2:')
result_vector1 = (my_tuple1[0] + my_tuple2[0], my_tuple1[1] + my_tuple2[1])

# Em không hiểu đáp án test case nên làm theo tích vô hướng
result_vector2 = my_tuple1[0] * my_tuple2[0] + my_tuple1[1] * my_tuple2[1] 
print("Result_vector1:", result_vector1)
print("Result_vector2:", result_vector2)

#Cau 3
print('Cau 3:')
distance = math.sqrt((my_tuple1[0] - my_tuple2[0]) ** 2 + (my_tuple1[1] - my_tuple2[1])**2)
print('Distance between vectors:', distance)

#Cau 4
print('Cau 4:')
index = ()

for value in my_tuple1:
    if value == 3:
        index += (my_tuple1.index(value), )

for value in my_tuple2:
    if value == 3:
        index += (my_tuple2.index(value), )

print('index=', index)

# Bag of words
print('Cau 5')
def corpus_to_string(corpus):
    return ' '.join(corpus)

def word_extraction(sentence):
    words = re.findall(r'\w+', sentence) 
    return words

def tokenize(sentence):
    words = []
    for word in word_extraction(sentence):
        words.append(word)
    return words

def convert_to_vector(sentence, vocab):
    vector = [0] * len(vocab)
    for word in tokenize(sentence):
        if word in vocab:
            vector[vocab.index(word)] += 1
    return vector



corpus = ["Tôi thích môn Toán", "Tôi thích AI", "Tôi thích âm nhạc"]
sentence = 'Tôi thích AI thích Toán'
vocab = sorted(set(tokenize(corpus_to_string(corpus))))
print('Tôi thích AI thích Toán', convert_to_vector(sentence, vocab))
print('Bag-Of-Words:', vocab)

# Search Algorithm
print('Cau 6:')
lst_data = [1, 1.1, None, 1.4, None, 1.5, None, 2.0]
result = []
for i in range(len(lst_data)):
    if lst_data[i] is None:
        result.append(i)

print('Vị trí None đầu tiên:', result[0])
print('Danh sách vị trí có giá trị None:', result)

#Time Series
print('Cau 7:')
data = [1, 1.1, None, 1.4, None, 1.5, None, 2.0]

first_valid = None
# Thêm 1 trường hợp nếu như None ở đầu
for i in range(len(data)):
    if data[i] is not None:
        first_valid = data[i]
        break

if first_valid is None:
    print('List is full with None, error')
else:
    for i in range(len(data)):
        if data[i] is None:
            if i == 0:  
                data[i] = first_valid
            else:
                data[i] = data[i - 1] 

print('Output:', data)

# Cau 8
print('Cau 8:')
lst_data = [
    [1 , 2 , 3] ,
    [4 , 5 , 6] ,
    [7 , 8 , 9] ,
]

lst_sub_data = []

for i in range(len(lst_data)):
    row = []
    for j in range(len(lst_data)):
        if j == 0 or j == 2:
            row.append(lst_data[i][j])
    lst_sub_data.append(row)

print('Output:', lst_sub_data)

# Cau 9:
print("Cau 9:")
def dot_product(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        return "Error: Kích thước ma trận không hợp lệ"
    
    n = len(A)
    res = [[0] * n for _ in range(n)]
    
    for i in range(n):  
        for j in range(n): 
            for k in range(n):
                res[i][j] += A[i][k] * B[k][j]  
    
    return res 

A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

B = np.array([
    [2, 4, 6],
    [1, 3, 5],
    [1, 0, 1]
])

Tong = A + B
Hieu = A - B
res1 = Tong.tolist() 
res2 = Hieu.tolist()
res3 = dot_product(A.tolist(), B.tolist())  

print("Tổng:", res1)
print("Hiệu:", res2)
print("Dot Product:", res3)

# Cau 10:
print('Cau 10:')
stop_words =["I", "love", "and", "to"]
input = "I love AI and listen to music"

words = input.split()
filtered_words = [word for word in words if word not in stop_words]
print('Output:', filtered_words)


#Normalization
print('Cau 11:')

def normalize(lst_data):
    min_val = min(lst_data)
    max_val = max(lst_data)
    return [(x - min_val) / (max_val - min_val) for x in lst_data]

test_cases = [
    [11 , 18 , 24 , 30 , 36] ,
    [50 , 100 , 150 , 200 , 250] ,
    [3 , 5 , 7 , 9 , 11]
    ]

for i, test_case in enumerate(test_cases):
    print(f"Test {i +1}: {normalize(test_case)}")
    
#Moving Average (Dung che GIF)
print('Cau 12:')
def moving_average(lst_data, k):
    result = [] 
    for i in range(k-1, len(lst_data)):
        sum_value = 0
        for j in range(i-k+1, i+1):
            sum_value += lst_data[j]
        avg = sum_value / k  
        result.append(avg)
    return result

test_cases = [
    ([1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9], 3),
    ([10 , 20 , 30 , 40 , 50 , 60 , 70], 4),
    ([5 , 10 , 15 , 20 , 25], 2)
]

for i, (test, k) in enumerate(test_cases):
    result = moving_average(test, k)
    print(f"Test {i + 1}: {result}")

#Tich Vo Huong
print('Cau 13:')
def dot_product(v1, v2):
    sum = 0
    for i in range(len(v1)):
        sum += v1[i] * v2[i]
    return sum

test_cases = [
 ([1 , 2 , 3] , [4 , 5 , 6]) ,
 ([2 , 4 , 6] , [1 , 3 , 5]) ,
 ([0 , 1 , 2] , [3 , 4 , 5])
 ]

for i , ( v1 , v2 ) in enumerate ( test_cases ):
 result = dot_product ( v1 , v2 )
 print ( f" Test {i +1}: { result }")


#Perceptron
print('Cau 14:')
def perceptron_relu(weights, inputs, bias):
    output = 0
    for i in range(len(weights)):
        output += weights[i] * inputs[i]
    output += bias
    
    result = max(0, output)
    return result

test_cases = [
    ([0.5 , -0.6 , 0.8] , [1.0 , 0.0 , 1.0] , -0.3) ,
    ([0.2 , 0.5 , -0.4] , [1.0 , 2.0 , -1.0] , 0.1) ,
    ([1.0 , -1.0 , 0.5] , [0.5 , 1.0 , -0.5] , -0.2)    
]

for i , ( weights , inputs , bias ) in enumerate ( test_cases ) :
 result = perceptron_relu ( weights , inputs , bias )
 print ( f" Test {i +1}: { result }")



        

        

