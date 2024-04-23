#!/usr/bin/python3
"""
Minimum Operations
"""


def minOperations(n):
    """
    calculates the fewest number of operations needed to result in exactly n H
    characters in the file
    """
    if n <= 1:
        return 0
    i = 2
    count = 0
    while i <= n:
        if n % i == 0:
            count += i
            n = n / i
        else:
            i += 1
    return count
