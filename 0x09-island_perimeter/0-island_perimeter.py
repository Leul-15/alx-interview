#!/usr/bin/python3
"""
Island Perimeter
"""


def island_perimeter(grid):
    """
    Description: returns the perimeter of the island described in grid
    """
    result = 0
    for row in range(len(grid)):
        for colu in range(len(grid[row])):
            if (grid[row][colu] == 1):
                val = 4
                if (row != 0 and grid[row - 1][colu] == 1):
                    val -= 1
                if (colu != len(grid[row]) - 1 and grid[row][colu + 1] == 1):
                    val -= 1
                if (colu != 0 and grid[row][colu - 1] == 1):
                    val -= 1
                if (row != len(grid) - 1 and grid[row + 1][colu] == 1):
                    val -= 1
                result += val
    return result
