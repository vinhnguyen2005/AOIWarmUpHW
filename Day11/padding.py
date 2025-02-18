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

def padding(mat_n):
    cols = len(mat_n[0])
    padding_matrix = [[0] * (cols + 2)] 
    
    padding_matrix += [[0] + x + [0] for x in mat_n]
    padding_matrix.append([0] * (cols + 2))
    return padding_matrix
    
    
mat_A = [[0,0,0],
         [0,4,0],
         [0,1,0]]

kernal = [[1,1], [1,1]]
print("Cau 1:", convolutional(padding(mat_A), kernal))
mat_C = [[0, 1, 0],
         [0, 1, 0],
         [0, 1, 0]]
print("Cau 2:", convolutional(padding(mat_A), mat_C))