#!/usr/bin/python3
"""
Module that defines the island_perimeter function.
"""


def island_perimeter(grid):
    """
    Return the perimeter of the island described in grid.

    Args:
        grid (list): List of lists of integers representing the map.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                perimeter += 4

                # Shared edge with the cell to the right
                if col < cols - 1 and grid[row][col + 1] == 1:
                    perimeter -= 2

                # Shared edge with the cell below
                if row < rows - 1 and grid[row + 1][col] == 1:
                    perimeter -= 2

    return perimeter
