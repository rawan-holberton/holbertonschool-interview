# N Queens

## Description

The **N Queens** project is an algorithmic challenge based on the classic chess puzzle of placing **N queens on an N×N chessboard** so that no two queens can attack each other.

A queen can attack another queen if they are placed on the same:
- Row
- Column
- Diagonal

The goal of this project is to write a program that finds and prints all possible solutions for the N Queens problem using a backtracking algorithm.

## Requirements

- All files are interpreted/compiled on **Ubuntu 14.04 LTS** using **Python 3.4.3**
- Allowed editors:
  - vi
  - vim
  - emacs
- All files must:
  - Start with the shebang:
    ```python
    #!/usr/bin/python3
    ```
  - End with a new line
  - Be executable
  - Follow **PEP 8 style guidelines (version 1.7.*)**
- A `README.md` file is mandatory at the root of the project
- Only the `sys` module can be imported

## Project Structure

````

nqueens/
│
├── 0-nqueens.py      # N Queens solver
└── README.md         # Project documentation

````

## Usage

Run the program with:

```bash
./0-nqueens.py N
````

Where:

* `N` is the size of the chessboard
* `N` must be an integer
* `N` must be greater than or equal to 4

## Input Validation

The program handles invalid inputs:

### Wrong number of arguments

Example:

```bash
./0-nqueens.py
```

Output:

```
Usage: nqueens N
```

Exit status:

```
1
```

### N is not an integer

Example:

```bash
./0-nqueens.py abc
```

Output:

```
N must be a number
```

Exit status:

```
1
```

### N is smaller than 4

Example:

```bash
./0-nqueens.py 3
```

Output:

```
N must be at least 4
```

Exit status:

```
1
```

## Algorithm

The solution uses **backtracking**:

1. Place a queen row by row.
2. Check if the position is safe:

   * No queen is in the same column.
   * No queen is on the same diagonal.
3. If the position is valid, continue placing the next queen.
4. If no valid position exists, backtrack and try another position.
5. Print every possible solution.

## Output Format

Each solution is printed on a single line.

The format is:

```python
[[row, column], [row, column], ...]
```

Each pair represents the position of a queen on the board.

Example:

```bash
./0-nqueens.py 4
```

Output:

```
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
```

Another example:

```bash
./0-nqueens.py 6
```

Output:

```
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
```

## Repository

GitHub repository:

`holbertonschool-interview`

Directory:

`nqueens`

File:

`0-nqueens.py`

## Author

By Rawan for Holberton School project N Queens
