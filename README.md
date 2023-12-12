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
## Usage/Examples

1. To solve the default grid press 1 and enter
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
```

## How it works <!-- Change this text -->

<!-- Enter stuff here -->
