#!/usr/bin/python3
"""
Rotate a 2D matrix 90 degrees clockwise.
"""


def rotate_2d_matrix(matrix):
    """
    Rotates an n x n 2D matrix 90 degrees clockwise.

    The rotation is done in-place without returning a new matrix.

    Args:
        matrix (list): A non-empty n x n 2D matrix.
    """
    n = len(matrix)

    # Transpose the matrix
    for row in range(n):
        for col in range(row, n):
            matrix[row][col], matrix[col][row] = (
                matrix[col][row],
                matrix[row][col]
            )

    # Reverse each row
    for row in range(n):
        matrix[row].reverse()
