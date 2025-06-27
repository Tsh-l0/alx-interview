#!/usr/bin/python3
"""
Choosing primes and removing them and their multiples
"""


def isWinner(x, nums):
    """
    Determines the winner of each round of the Prime Game

    Args:
        x (int): The number of rounds.
        nums (list of int): A list of integers where each integer n denotes
        a set of consecutive integers starting from 1 up to and including n.

    Returns:
        str: The name of the player who won the most rounds (either "Ben"
        or "Maria").
        None: If there is no winner

    Raises:
        None
    """
    # Check for invalid input
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None

    # Initialize scores and array of prime nums
    ben = 0
    maria = 0
    a = [1 for x in range(sorted(nums)[-1] + 1)]
    a[0], a[1] = 0, 0

    for i in range(2, len(a)):
        rm_multiples(a, i)

    for i in nums:
        if sum(a[0:i + 1]) % 2 == 0:
            ben += 1
        else:
            maria += 1

    # Determine the winner of the game
    if ben > maria:
        return "Ben"
    if maria > ben:
        return "Maria"
    return None


def rm_multiples(ls, x):
    """
    Removes multiples of a prime number from an array of possible prime
    numbers
    """
    for i in range(2, len(ls)):
        try:
            ls[i * x] = 0
        except (ValueError, IndexError):
            break
