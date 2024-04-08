#!/usr/bin/python3
"""
Function to calculate the perimeter of the island described in a grid.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island.

    Args:
        grid (list of list of int): Represents the island grid.

    Returns:
        int: Perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows else 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    return perimeter
