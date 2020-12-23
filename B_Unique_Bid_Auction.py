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

    num, mxn, idx = defaultdict(int), 999999999, -1    
    for i in a:
        num[i] = num.get(i, 0) + 1                   # num[i] += 1 can also be !
    
    for i in range(n):
        if (mxn > a[i]) and (num[a[i]] == 1):
            idx = i+1
            mxn = a[i]

    print(idx)

