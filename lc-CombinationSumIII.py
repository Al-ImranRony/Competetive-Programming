# LeetCode Sept challenge 12

import sys
import math
import heapq
import random
import collections
from collections import Counter, defaultdict
from itertools import combinations, permutations


def combinationSum3(k, n):
    return [comb for comb in combinations(range(1, 10), k) if sum(comb) == n]


print(combinationSum3(3, 7))
print(combinationSum3(3, 9))