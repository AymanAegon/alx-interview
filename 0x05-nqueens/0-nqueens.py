#!/usr/bin/python3
"""
0x05. N Queens
"""
import sys

NUMBER_OF_ARGS = len(sys.argv)
if NUMBER_OF_ARGS != 2:
    print("Usage: nqueens N")
    exit(1)

N = sys.argv[1]
try:
    N = int(N)
except Exception:
    print("N must be a number")
    exit(1)

if N < 4:
    print("N must be at least 4")
    exit(1)


def reject(list, pos):
    """reject a position"""
    for p in list:
        if p[0] == pos[0] or p[1] == pos[1]:
            return True
        if (p[0] + p[1]) == (pos[0] + pos[1]):
            return True
        if (p[0] - p[1]) == (pos[0] - pos[1]):
            return True
    return False


def accept(list, pos):
    """accept a position"""
    return not reject(list, pos)


def backtrack(list, pos):
    """"""
    if len(list) == N:
        return list
    if accept(list, pos):
        list.append(pos)
    else:
        pass
