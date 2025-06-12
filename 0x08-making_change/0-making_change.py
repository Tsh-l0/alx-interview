#!/usr/bin/python3
"""
Code for solving a coin change problem using dynamic programming
Given a pile of coins of different values, determine the fewest number
of coins needed to meet a given amount total
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins necessary to meet a given total

    Args:
        coins (list): List of coin denominations available
        total (int): Target amount to make change for

    Returns:
        int: Fewest number of coins needed to meet total
            Returns -1 if total cannot be met by any number of coins
            Returns 0 if total is 0 or less
    """
    if not coins or coins is None:
        return -1
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Fill the dp array for each amount from 1 to total
    for amount in range(1, total + 1):
        for coin in coins:
            if coin <= amount and dp[amount - coin] != float('inf'):
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # Return result: -1 if impossible, otherwise minimum coins needed
    return dp[total] if dp[total] != float('inf') else -1
