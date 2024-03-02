#!/usr/bin/python3
"""
0. Change comes from within
"""
import sys
from typing import List


def minCoinsUtil(coins, m, V, dp):
    """"""
    if V == 0:
        return 0
    if dp[V] != -1:
        return dp[V]
    res = sys.maxsize
    for i in range(m):
        if coins[i] <= V:
            sub_res = minCoinsUtil(coins, m, V - coins[i], dp)
            if sub_res != sys.maxsize and sub_res + 1 < res:
                res = sub_res + 1
    dp[V] = res
    return res


def minCoins(coins, m, V):
    """"""
    dp = [-1] * (V + 1)
    return minCoinsUtil(coins, m, V, dp)


def makeChange(coins: List, total: int) -> int:
    """
    Given a pile of coins of different values,
    determines the fewest number of coins needed to meet a given amount total.
    """
    if total <= 0:
        return 0

    res = minCoins(coins, len(coins), total)
    if res > total:
        return -1
    return res
