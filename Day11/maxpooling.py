#max pooling
def maxpooling(mat_n, size = 2, stride = 2):
    row_n = len(mat_n)
    col_n = len(mat_n[0])
    
    output = []
    for i in range(0, row_n-size+1, stride):
        row = []
        for j in range(0, col_n-size+1, stride):
            sub_matrix = [mat_n[i+k][j+l] for k in range(size) for l in range (size)]
            row.append(max(sub_matrix))
        output.append(row)
    return output


def avg_pooling(mat_n, size = 2, stride = 2):
    row_n = len(mat_n)
    col_n = len(mat_n[0])
    output = []
    for i in range(0, row_n-size+1, stride):
        row = []
        for j in range(0, col_n-size+1, stride):
            sub_matrix = [mat_n[i+k][j+l] for k in range(size) for l in range (size)]
            avg = sum(sub_matrix) / (size * size)
            row.append(avg)
        output.append(row)
    return output
    
    

mat_A = [[0,0,0,4], [0,4,0,2], [0,1,0,2],[0,3,0,2]]

print("Cau 1:", maxpooling(mat_A))
print("Cau 2:", avg_pooling(mat_A))
