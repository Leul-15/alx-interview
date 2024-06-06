#!/usr/bin/python3
"""
Module find the fewest number of coins needed to meet a given amount total
"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values, determine the fewest number of
    coins needed to meet a given amount total
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
