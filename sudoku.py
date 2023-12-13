def solve(board): # if board is solved returns True otherwise returns False
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
                return True # when a number has been inserted successfully it returns True
            else:
                board[row][col] = 0 # when a number cannot be inserted, reset previous number to 0, continue for loop iteration for previous recursive call of solve() until a different number is inserted that is valid
    # NO VALID MOVES FOUND in position of first zero, then statement below is run
    return False # into line 15 | if solve(board): recives False, else block above is run
def isValid(board, num, pos): # if move is valid returns True otherwise returns False
    for i in range(9): # 9 = no. of columns
        if board[pos[0]][i] == num:
            return False
    for i in range(9): # 9 = no. of rows
        if board[i][pos[1]] == num:
            return False
    box_x = (pos[0] // 3) * 3
    box_y = (pos[1] // 3) * 3
    for i in range(box_x, box_x + 3):
        for j in range(box_y, box_y + 3):
            if board[i][j] == num:
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
    return False # if no 0s present in sudoku
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
def runProgram():
    print("\nSudoku Entered:\n")
    print_board(board)
    solve(board)
    print("\nSolution:\n")
    if emptyCheck(board):
        print("The Sudoku entered is unsolvable!")
    else:
        print_board(board)
def isInput_valid():
    try:
        givenInput = eval("[" + input(f"Enter row no. {row_no} of Sudoku: ") + "]")
        for num in givenInput:
            if num > 9 or num < 0:
                print(f"Error: Invalid input please enter integers between 0-9 (inclusive)")
                print("Example input: 0, 6, 9, 0, 0, 0, 0, 7, 8")
                return isInput_valid()
        if (len(givenInput) != 9):
            print(f"Error: Invalid input please enter nine values separated by a comma, only {len(givenInput)} given")
            print("Example input: 0, 6, 9, 0, 0, 0, 0, 7, 8")
            return isInput_valid()
    except:
        print("Error: Invalid input please enter integers between 0-9 (inclusive)")
        print("Example input: 0, 6, 9, 0, 0, 0, 0, 7, 8")
        return isInput_valid()
    return givenInput
while True:
    print("\n# Menu")
    print("1. Solve default sudoku")
    print("2. Solve user-entered sudoku")
    print("3. Exit")
    choice = int(input("Select next action (1/2/3): "))
    if choice == 1:
        runProgram()
    elif choice == 2:
        board = []
        for row_no in range(1, 10):
            row = isInput_valid()
            board.append(row)
        runProgram()
    elif choice == 3:
        quit("Thank you for using Sudoku solver. Have a great day!")
    else:
        print("Error: Invalid input please enter 1, 2 or 3")