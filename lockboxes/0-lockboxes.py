#!/usr/bin/python3
"""
Module that contains the canUnlockAll function.
"""


def canUnlockAll(boxes):
    """
    Determine if all boxes can be opened.

    Args:
        boxes (list): List of boxes containing keys.

    Returns:
        bool: True if all boxes can be opened, otherwise False.
    """
    opened = {0}
    keys = [0]

    while keys:
        box = keys.pop()

        for key in boxes[box]:
            if key < len(boxes) and key not in opened:
                opened.add(key)
                keys.append(key)

    return len(opened) == len(boxes)
