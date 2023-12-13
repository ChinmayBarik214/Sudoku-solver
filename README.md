# Sudoku Solver using Python

## Python code which uses recursion and backtracking to solve any sudoku entered by the user

This project is my submission for the practical exam under the subject of _Software Craftsmanship Lab_ during the first semester of my _B. Tech CSE (Full Stack Development)_ degree. This project can be used in real-world scenarios through the following ways:

- To verify one’s sudoku solution
- To understand the backtracking algorithm
- To instantly solve any sudoku
- To check wether a sudoku is solvable or not

## Run Locally

[Clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) this project

```bash
  git clone https://github.com/ChinmayBarik214/Sudoku-solver
```

Go to its project directory

```bash
  cd Sudoku-solver
```

Ensure [python](https://www.python.org/downloads/) is installed and run sudoku.py

```bash
  python sudoku.py
```

## Usage

1. To solve the default sudoku press 1 followed by enter
2. To solve a user-entered sudoku press 2 followed by enter
   - You will then be prompted to enter the sudoku row-by-row
   - Enter each row in [CSV](https://en.wikipedia.org/wiki/Comma-separated_values) format, i.e., enter the first value followed by a comma then the second value followed by a comma and so on
   - Example input for 1st row: `0, 6, 9, 0, 0, 0, 0, 7, 8`
   - After you have finished typing a row press enter to start typing the next row and so on until all nine rows have been entered
   - Now your sudoku will be solved in under five seconds and its solution will be displayed!
   - In case you have entered an unsolvable sudoku the following message will be displayed `The Sudoku entered is unsolvable!`
3. To exit the application press 3 followed by enter

## Demo

```
# Menu
1. Solve default sudoku
2. Solve user-entered sudoku
3. Exit
Select next action (1/2/3): 1

Sudoku Entered:

0 6 9 | 0 0 0 | 0 7 8
5 0 0 | 0 4 0 | 0 0 0
0 0 0 | 0 0 7 | 6 0 5
------+-------+------
9 4 2 | 7 0 3 | 1 0 6
7 0 6 | 5 0 2 | 8 4 3
0 0 0 | 1 0 4 | 0 9 0
------+-------+------
0 0 0 | 0 0 6 | 0 8 0
6 0 1 | 0 3 9 | 0 0 0
0 5 4 | 0 7 0 | 3 0 0

Solution:

1 6 9 | 3 2 5 | 4 7 8
5 3 7 | 6 4 8 | 9 1 2
4 2 8 | 9 1 7 | 6 3 5
------+-------+------
9 4 2 | 7 8 3 | 1 5 6
7 1 6 | 5 9 2 | 8 4 3
3 8 5 | 1 6 4 | 2 9 7
------+-------+------
2 9 3 | 4 5 6 | 7 8 1
6 7 1 | 8 3 9 | 5 2 4
8 5 4 | 2 7 1 | 3 6 9

# Menu
1. Solve default sudoku
2. Solve user-entered sudoku
3. Exit
Select next action (1/2/3): 2
Enter row no. 1 of Sudoku: 0, 8, 0, 0, 0, 6, 2, 0, 0
Enter row no. 2 of Sudoku: 5, 0, 0, 8, 7, 0, 3, 0, 0
Enter row no. 3 of Sudoku: 0, 0, 0, 0, 0, 4, 0, 7, 0
Enter row no. 4 of Sudoku: 0, 4, 0, 2, 1, 0, 0, 3, 0
Enter row no. 5 of Sudoku: 0, 0, 9, 0, 0, 0, 5, 0, 0
Enter row no. 6 of Sudoku: 0, 0, 0, 0, 0, 7, 0, 0, 0
Enter row no. 7 of Sudoku: 0, 0, 0, 6, 0, 0, 0, 0, 0
Enter row no. 8 of Sudoku: 0, 2, 0, 3, 8, 0, 0, 1, 0
Enter row no. 9 of Sudoku: 4, 0, 0, 0, 0, 0, 0, 0, 2

Sudoku Entered:

0 8 0 | 0 0 6 | 2 0 0
5 0 0 | 8 7 0 | 3 0 0
0 0 0 | 0 0 4 | 0 7 0
------+-------+------
0 4 0 | 2 1 0 | 0 3 0
0 0 9 | 0 0 0 | 5 0 0
0 0 0 | 0 0 7 | 0 0 0
------+-------+------
0 0 0 | 6 0 0 | 0 0 0
0 2 0 | 3 8 0 | 0 1 0
4 0 0 | 0 0 0 | 0 0 2

Solution:

7 8 4 | 1 3 6 | 2 9 5
5 6 2 | 8 7 9 | 3 4 1
3 9 1 | 5 2 4 | 8 7 6
------+-------+------
6 4 5 | 2 1 8 | 7 3 9
1 7 9 | 4 6 3 | 5 2 8
2 3 8 | 9 5 7 | 1 6 4
------+-------+------
8 1 7 | 6 4 2 | 9 5 3
9 2 6 | 3 8 5 | 4 1 7
4 5 3 | 7 9 1 | 6 8 2

# Menu
1. Solve default sudoku
2. Solve user-entered sudoku
3. Exit
Select next action (1/2/3): 3
Thank you for using Sudoku solver. Have a great day!
```

## Algorithm

To solve this puzzle at any difficulty level the Sudoku Solver makes use of a backtracking algorithm. At a macro level this can be explained as follows:

1. Find the first `0` (empty space) on the board going row-by-row and return its position.
2. The first integer out of 1-9 which is a valid move in this positoin i.e., is unique within its row, column, and box/subgrid is placed there.
   - After the number is inserted the loop which was providing values 1-9 is not terminated.
   - This is because if it is later found that the value inserted here was not the one in the final solution (even though it was a valid move at this point) then the loop will continue execution (See step 4).
3. Steps 1 & 2 are now repeated on the new grid thus obtained.
   - The 1st `0` found on the new grid will be the 2nd `0` on the initial grid
   - The 1st `0` found on the grid created after that will be the 3rd `0` on the initial grid and so on this process will repeat until a position is found where no number 1-9 is a valid move.
4. In this case the previous move will continue running step 2 but it will continue from the last number it inserted instead of 1-9.
   - In simple words, if the numbers 2, 3, 7 all were valid moves, Sudoku Solver will first try 2, but if later on it is found that 2 is resulting in the formation of an unsolvable sudoku, then it will try 3 instead, if the same issue occurs for 3 it will try again with 7.
   - If the issue keeps occuring for every valid move then we declare the sudoku unsolvable.
   - Otherwise we continue execution until there are no longer any 0s found on the board, i.e., the sudoku is solved.

### Visual Helper
1. You may uncomment [lines 4-6 of sudoku.py](https://github.com/ChinmayBarik214/Sudoku-solver/blob/50316bd2ec8a40c45b63024d32dcfa9f89172f13/sudoku.py#L4-L6) on your system and run the program to see the sudoku after each recursive call of `solve(board)`
2. Doing so for the default sudoku will lead to the execution of the steps explained through the following visual:

![Visual Helper]()
