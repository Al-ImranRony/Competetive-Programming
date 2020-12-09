# Codechef Dec Challenge

import sys
import math
import heapq 
import random
import collections
from collections import Counter, defaultdict
from itertools import combinations, permutations

for _ in range(int(input())):
    a, b = map(int, input().split())
    evPair, i, j = 0, 1, 1
    while (i<=a and j<=b):
        if (i + j)%2 == 0: evPair += 1
        print(i, j)
        i, j = i+1, j+1
    print(evPair)