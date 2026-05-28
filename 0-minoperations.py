#!/usr/bin/python3
"""
Module that calculates the minimum number of operations
to result in exactly n 'H' characters using Copy All and Paste.
"""


def minOperations(n):
    """
    Returns the minimum number of operations needed to reach n characters.

    Args:
        n (int): Target number of 'H' characters

    Returns:
        int: Minimum number of operations, or 0 if impossible
    """
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
