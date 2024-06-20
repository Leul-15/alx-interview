#!/usr/bin/python3
"""Prime Game"""


def isWinner(x, nums):
    """
    Tell Winner
    """

    name = {'Maria': 0, 'Ben': 0}
    for i in range(x):
        if (prime_number(nums[i]) % 2 == 0):
            name['Ben'] += 1
        else:
            name['Maria'] += 1
    if (name['Ben'] > name['Maria']):
        return 'Ben'
    elif (name['Ben'] < name['Maria']):
        return 'Maria'
    else:
        return None


def prime_number(number):
    """
    Calculate number of prime number
    """
    if number <= 0:
        return 0
    prime = [True for i in range(number + 1)]
    p = 2
    while p * p <= number:
        if prime[p]:
            for i in range(p * 2, number + 1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False
    count = 0
    for i in range(number + 1):
        if prime[i]:
            count += 1
    return count
