#!/usr/bin/python3
"""Pascal triangle"""


def pascal_triangle(n):
    """Calculate pascals triangle"""
    result = [[1]]

    if n <= 0:
        return []

    for i in range(n - 1):
        last_row = [0] + result[-1] + [0]
        current_row = []
        for j in range(len(result[-1]) + 1):
            current_row.append(last_row[j] + last_row[j + 1])
        result.append(current_row)
    return result
