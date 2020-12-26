# December lunchtime 2020 A

import sys
import math
import heapq 
import random
import collections
from collections import Counter, defaultdict, deque
from itertools import combinations, permutations

for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    s = sum(arr)
    if (s % k == 0):
        print(0)
    else:
        print(1)

