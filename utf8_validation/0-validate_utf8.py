#!/usr/bin/python3
"""
UTF-8 validation module.
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list): List of integers representing bytes.

    Returns:
        bool: True if data is valid UTF-8, otherwise False.
    """
    num_bytes = 0

    for num in data:
        byte = num & 0xFF

        if num_bytes == 0:
            mask = 0x80

            while mask & byte:
                num_bytes += 1
                mask >>= 1

            if num_bytes == 0:
                continue

            if num_bytes == 1 or num_bytes > 4:
                return False

            num_bytes -= 1
        else:
            if (byte & 0xC0) != 0x80:
                return False

            num_bytes -= 1

    return num_bytes == 0
