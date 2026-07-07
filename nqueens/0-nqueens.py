#!/usr/bin/python3
"""
N Queens puzzle solver.
"""

import sys


def is_safe(queens, row, col):
    """
    Check if a queen can be placed at (row, col).
    """
    for r, c in queens:
        if c == col or abs(r - row) == abs(c - col):
            return False
    return True


def solve_nqueens(n, row, queens):
    """
    Solve the N Queens puzzle using backtracking.
    """
    if row == n:
        print([[r, c] for r, c in queens])
        return

    for col in range(n):
        if is_safe(queens, row, col):
            queens.append([row, col])
            solve_nqueens(n, row + 1, queens)
            queens.pop()


def main():
    """
    Validate arguments and start the solver.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(n, 0, [])


if __name__ == "__main__":
    main()
