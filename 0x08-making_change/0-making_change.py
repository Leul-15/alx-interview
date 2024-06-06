#!/usr/bin/python3
"""
"""


def makeChange(coins, total):
    """
    """
    number = 0
    count = 0
    if total <= 0:
        return 0
    coins = sorted(coins, reverse=True)
    for value in coins:
        while (total >= number + value):
            number += value
            count += 1
        if number == total:
            return count
        elif number > total:
            return -1
    return -1
