#!/usr/bin/python3
"""UTF-8 validation module.
"""


def validUTF8(data):
    """Checks if a list of integers are valid UTF-8 codepoints.
    """
    skip_count = 0
    data_length = len(data)
    for i in range(data_length):
        if skip_count > 0:
            skip_count -= 1
            continue
        if type(data[i]) != int or data[i] < 0 or data[i] > 0x10FFFF:
            return False
        elif data[i] <= 0x7F:
            skip_count = 0
        elif data[i] & 0b11111000 == 0b11110000:
            span = 4
            if data_length - i >= span:
                next_bytes = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[i + 1: i + span],
                ))
                if not all(next_bytes):
                    return False
                skip_count = span - 1
            else:
                return False
        elif data[i] & 0b11110000 == 0b11100000:
            span = 3
            if data_length - i >= span:
                next_bytes = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[i + 1: i + span],
                ))
                if not all(next_bytes):
                    return False
                skip_count = span - 1
            else:
                return False
        elif data[i] & 0b11100000 == 0b11000000:
            span = 2
            if data_length - i >= span:
                next_bytes = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[i + 1: i + span],
                ))
                if not all(next_bytes):
                    return False
                skip_count = span - 1
            else:
                return False
        else:
            return False
    return True
