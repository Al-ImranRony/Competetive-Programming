# LeetCode Sept challenge 11

import sys
import math
import heapq
import random
import collections
from collections import Counter, defaultdict
from itertools import combinations, permutations


def maxProduct(nums) -> int:
    res, maxi, mini = -math.inf, 1, 1

    for i in nums:
        a, b = maxi * i, mini * i
        maxi, mini = max(a, b, i), min(a, b, i)
        res = max(res, maxi)

    return res


print(maxProduct([2, 3, -2, 4]))
print(maxProduct([-2, 0, -1]))
print(maxProduct([-2, 0, 8, 9, -1]))

