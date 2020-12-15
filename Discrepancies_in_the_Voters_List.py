# Day 15 of 100DaysOfCode

import sys
import math
import heapq 
import random
import collections
from collections import Counter, defaultdict
from itertools import combinations, permutations


n1, n2, n3 = (map(int, input().split()))
dl, fl = [], []
for i in range(n1+n2+n3):
    id = int(input())
    dl.append(id)

dl = Counter(dl)
for j in dl.keys():
    if dl[j] != 1:
        fl.append(j)

print(len(fl))
fl.sort()
for k in fl:
    print(k)