def solve(board):
    found0 = emptyCheck(board)
    if not found0:
        return True
    else:
        row, col = found0 # (row, col)-index of first zero found in sudoku
    for i in range(1, 10):
        if isValid(board, i, (row, col)):
            board[row][col] = i
            if solve(board):
                return True
            board[row][col] = 0
    return False
def isValid(board, num, pos):
    for i in range(9): # 9 = no. of columns
        if board[pos[0]][i] == num and pos[1] != i: # check every column in the row in which the first zero has been found except 1st/2nd/3rd/.../9th column for num to be entered
            return False # if num is already there move is invalid
    for i in range(9): # 9 = no. of rows
        if board[i][pos[1]] == num and pos[0] != i: # check every row in the column in which the first zero has been found except 1st/2nd/3rd/.../9th column for num to be entered
            return False # if num is already there move is invalid
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False
    return True
def print_board(board):
    for i in range(9): # 9 = no. of rows
        if i % 3 == 0 and i != 0:
            print("------+-------+------") # horizontal line + "\n" before 4th & 7th row
        for j in range(9): # 9 = no. of columns
            if j % 3 == 0 and j != 0:
                print("| ", end="") # "|" + " " before 4th & 7th column
            if j == 8:
                print(board[i][j]) # number + "/n" for last column numbers
            else:
                print(str(board[i][j]) + " ", end="") # number + " " for non-last column numbers
def emptyCheck(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j) # (row, col)-index of first zero found in sudoku
    return None # if no 0s present in sudoku
board = [
[0, 8, 0, 0, 0, 6, 2, 0, 0],
[5, 0, 0, 8, 7, 0, 3, 0, 0],
[0, 0, 0, 0, 0, 4, 0, 7, 0],
[0, 4, 0, 2, 1, 0, 0, 3, 0], 
[0, 0, 9, 0, 0, 0, 5, 0, 0],
[0, 0, 0, 0, 0, 7, 0, 0, 0],  
[0, 0, 0, 6, 0, 0, 0, 0, 0],
[0, 2, 0, 3, 8, 0, 0, 1, 0],
[4, 0, 0, 0, 0, 0, 0, 0, 2] 
] 
# Uncomment below code to input sudoku from user:

# board = []
# for row_no in range(1, 10):
#     row = eval(input(f"Enter row no. {row_no} of Sudoku:"))
#     board.append(row)
print("\nSudoku Entered:\n")
print_board(board)
solve(board)
print("\nSolution:\n")
print_board(board)