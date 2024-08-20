#!/usr/bin/python3
"""
uses greedy algorithm to make change for a given amount of money
"""

def makeChange(coins, total):
    """
    makes change for a given amount of money
    """
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    num_coins = 0
    for coin in coins:
        if total <= 0:
            break
        num_coins += total // coin
        total = total % coin
    if total != 0:
        return -1
    return num_coins