N = 5  

dx = [2, 1, -1, -2, -2, -1, 1, 2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

def is_valid_move(x, y, board):
    return 0 <= x < N and 0 <= y < N and board[x][y] == -1

def knight_tours(x, y, move_count, board):
    if move_count > N*N:
        return True
    
    for i in range(8):
        new_x = x + dx[i]
        new_y = y + dy[i]
        if is_valid_move(new_x, new_y, board):
            board[new_x][new_y] = move_count
            if knight_tours(new_x, new_y, move_count + 1, board):
                return True
            board[new_x][new_y] = -1
            
    return False

def print_matrix(board):
    for row in board:
        print(row)
        

def solve_knight_tours(x , y):
    board = [[-1]*N for _ in range(N)]
    board[x][y] = 1
    if knight_tours(x, y, 2, board):
        print_matrix(board)
    else:
        print("No solution exists")

solve_knight_tours(0,0)   