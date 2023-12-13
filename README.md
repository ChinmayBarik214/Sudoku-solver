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

To solve even the most challenging of these puzzles, our Sudoku solver only needs to follow three strategies:

1. If a square has only one candidate, place that value there.
2. If a candidate is unique within a row, box or column, place that value there (hidden singles).
3. If neither 1 or 2 is true in the entire grid, make a guess. Backtrack if the Sudoku becomes unsolvable.

<!-- The code also implements a check to determine if the Sudoku is solvable. This is run at the start of each solving task. --> <!-- Maybe add this? -->

<!-- Enter stuff here -->
