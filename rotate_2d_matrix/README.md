# Rotate 2D Matrix

## Description

This project implements an algorithm to rotate an **n × n 2D matrix** by **90 degrees clockwise**.

The matrix must be modified **in-place**, meaning the function should update the original matrix directly without creating and returning a new matrix.

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
  - Follow **PEP 8 style guidelines (version 1.7.x)**
- A `README.md` file is mandatory at the root of the project
- No modules can be imported
- All modules and functions must be documented

## Project Structure

````

rotate_2d_matrix/
│
├── 0-rotate_2d_matrix.py    # Matrix rotation algorithm
└── README.md               # Project documentation

````

## Task

### 0. Rotate 2D Matrix

Write a function:

```python
def rotate_2d_matrix(matrix):
````

that rotates an `n × n` 2D matrix **90 degrees clockwise**.

### Parameters

* `matrix`

  * A non-empty 2-dimensional list
  * The matrix size is `n × n`

### Return

* The function does not return anything.
* The original matrix is modified directly.

## Algorithm

The rotation is performed in-place using two main steps:

1. **Transpose the matrix**

   * Convert rows into columns.

2. **Reverse each row**

   * Reverse the order of elements in each row to obtain the clockwise rotation.

Example:

Before rotation:

```
[
 [1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]
]
```

After a 90-degree clockwise rotation:

```
[
 [7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]
]
```

## Usage

Example:

```python
#!/usr/bin/python3

rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

rotate_2d_matrix(matrix)
print(matrix)
```

Output:

[
 [7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]
]


## Repository

GitHub repository:

`holbertonschool-interview`

Directory:

`rotate_2d_matrix`

File:

`0-rotate_2d_matrix.py`

## Author

By Rawan fro Holberton School project Rotate 2D Matrix
