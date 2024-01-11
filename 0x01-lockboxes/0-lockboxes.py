#!/usr/bin/python3
"""
0. Lockboxes
"""


def canUnlockAll(boxes):
    """
    Return True if all boxes can be opened, else return False
    """
    keys = [0]
    for i in range(len(boxes)):
        if i not in keys:
            return False
        print(i)
        for key in boxes[i]:
            if key not in keys:
                keys.append(key)
    return True
