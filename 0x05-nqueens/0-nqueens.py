#!/usr/bin/python3
"""
N queens
"""

import sys

if len(sys.argv) != 2:
    print('Usage: nqueens N')
    exit(1)

try:
    n_queens = int(sys.argv[1])
except ValueError:
    print('N must be a number')
    exit(1)

if n_queens < 4:
    print('N must be at least 4')
    exit(1)


def solve_nqueens(num):
    '''self descriptive'''
    if num == 0:
        return [[]]
    inner_solution = solve_nqueens(num - 1)
    return [solution + [(num, i + 1)]
            for i in range(n_queens)
            for solution in inner_solution
            if safe_queen((num, i + 1), solution)]


def attack_queen(square, queen):
    '''self descriptive'''
    (row1, col1) = square
    (row2, col2) = queen
    return (row1 == row2) or (col1 == col2) or\
        abs(row1 - row2) == abs(col1 - col2)


def safe_queen(sqr, queens):
    '''self descriptive'''
    for queen in queens:
        if attack_queen(sqr, queen):
            return False
    return True


for answer in reversed(solve_nqueens(n_queens)):
    result = []
    for p in [list(p) for p in answer]:
        result.append([i - 1 for i in p])
    print(result)
