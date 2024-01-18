#!/usr/bin/python3
'''
0. Minimum Operations
'''


def minOperations(n):
    '''
    calculates the fewest number of operations needed
    to result in exactly n H characters in the file.
    '''
    current_count = 1
    clipboard = 0
    operation_count = 0

    while current_count < n:
        if clipboard == 0:
            clipboard = current_count
            operation_count += 1

        if current_count == 1:
            current_count += clipboard
            operation_count += 1
            continue

        remaining = n - current_count
        if remaining < clipboard:
            return 0

        if remaining % current_count != 0:
            current_count += clipboard
            operation_count += 1
        else:
            clipboard = current_count
            current_count += clipboard
            operation_count += 2

    if current_count == n:
        return operation_count
    else:
        return 0
