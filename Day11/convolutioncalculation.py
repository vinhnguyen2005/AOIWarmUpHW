def convolutional(mat_A, mat_B):
    n_rows = len(mat_A) - len(mat_B) + 1
    n_cols = len(mat_A[0]) - len(mat_B[0]) + 1
    res = []
    for i in range(n_rows):
        row = []
        for j in range(n_cols):
            sum = 0
            for k in range(len(mat_B)):
                for l in range(len(mat_B[0])):
                    sum += mat_A[i+k][j+l] * mat_B[k][l]
            row.append(sum)
        res.append(row)
        
    return res


mat_A =  [[1,2,3],
          [4,5,6],
          [7,8,9]]

kernal = [[2,4],
          [1, 3]]

#Cau 1:
print("Cau 1:",convolutional(mat_A, kernal))
mat_C = [[1, 1, 1],
         [0, 0, 0],
         [1, 1,1]]
#Cau 2:
print("Cau 2:", convolutional(mat_A, mat_C)[0])


