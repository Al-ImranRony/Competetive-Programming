# LeetCode playground template


import sys
import math
import heapq 
import random
import collections
from collections import Counter, defaultdict, deque
from itertools import combinations, permutations


def yourFunc(s, wordDict) -> bool:
    n = len(s)
    dp = [i == 0 for i in range(n+1)]         

    for i in range(n):
        if dp[i]:
            for j in range(i+1, n+1):
                if (s[i:j] in wordDict): dp[j] = True

    return dp[-1]


print(yourFunc("leetcode", ["leet", "code"]))
