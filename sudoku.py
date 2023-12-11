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
            board[row][col] = i # Try 1/2/…/9 and replace first zero found on board with the first number found from 1-9 which is valid in the zero’s position
            if solve(board): # Run solve function again with a new board created by inserting a number to the previous board
                return # exits the function when solve(board) returns True, i.e., the sudoku is solved (base case reached)
            else:
                board[row][col] = 0 # replace the first zero with zero?
    # NO VALID MOVES FOUND in position of first zero, then statement below is run
    return False # into line 15 | if solve(board): recives False, else block above is run
def isValid(board, num, pos): # if move is valid returns True otherwise returns False
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
    for i in range(9): # 9 = no. of rows
        for j in range(9): # 9 = no. of columns
            if board[i][j] == 0:
                return (i, j) # (row, col)-index of first zero found in sudoku
    return None # if no 0s present in sudoku
board = [
[8, 9, 4, 0, 0, 0, 0, 5, 1],
[0, 0, 7, 0, 0, 3, 0, 6, 9],
[0, 6, 0, 5, 0, 4, 0, 0, 0],
[0, 3, 8, 4, 5, 1, 0, 0, 0], 
[2, 0, 0, 0, 0, 6, 8, 0, 5],
[6, 0, 0, 0, 0, 2, 7, 0, 0],  
[3, 8, 0, 1, 7, 5, 0, 0, 0],
[4, 0, 0, 3, 6, 9, 1, 0, 8],
[0, 1, 0, 0, 0, 0, 5, 7, 0] 
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