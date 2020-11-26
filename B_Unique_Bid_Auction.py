# Codeforces Round 686, Div3 - b

import sys
import math
import heapq 
import random
import collections
from collections import Counter, defaultdict
from itertools import combinations, permutations


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    m, mark = 200000, [0] * (n+1)
    print(mark)
    for i in range(1, n+1):
        mark[a[i]] += 1
    print(mark)
