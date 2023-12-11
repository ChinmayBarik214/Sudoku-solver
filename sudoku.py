def solve(board):
    # Uncomment below code to see board after each recursion
    #
    # print("\n")
    # print_board(board)
    # print("\n")
    found0 = emptyCheck(board)
    if not found0:
        return True # indicates that solution has been found (base case of recursion)
    else:
        row, col = found0 # (row, col)-index of first zero found in sudoku
    for i in range(1, 10):
        if isValid(board, i, (row, col)):
            board[row][col] = i # Try 1/2/…/9 and replace first zero found on board with the first number which is valid there
            if solve(board):
                return True
            board[row][col] = 0 # Reset the last number we added to 0 and try a different number there
    return False
def isValid(board, num, pos):
    for i in range(9): # 9 = no. of columns
        if board[pos[0]][i] == num and pos[1] != i:
            return False
    for i in range(9): # 9 = no. of rows
        if board[i][pos[1]] == num and pos[0] != i:
            return False
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
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
[0, 6, 9, 0, 0, 0, 0, 7, 8],
[5, 0, 0, 0, 4, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 7, 6, 0, 5],
[9, 4, 2, 7, 0, 3, 1, 0, 6], 
[7, 0, 6, 5, 0, 2, 8, 4, 3],
[0, 0, 0, 1, 0, 4, 0, 9, 0],  
[0, 0, 0, 0, 0, 6, 0, 8, 0],
[6, 0, 1, 0, 3, 9, 0, 0, 0],
[0, 5, 4, 0, 7, 0, 3, 0, 0] 
]
# Uncomment below code to input sudoku from user:
#
# board = []
# for row_no in range(1, 10):
#     row = eval(input(f"Enter row no. {row_no} of Sudoku:"))
#     board.append(row)
print("\nSudoku Entered:\n")
print_board(board)
solve(board)
print("\nSolution:\n")
print_board(board)