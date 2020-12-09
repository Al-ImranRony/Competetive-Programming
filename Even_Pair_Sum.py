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
    for i in range(1, a+1):
        if (i%2) == 0: 
            for j in range(2, b+1, 2):
                if ((i+j)%2) == 0: evPair += 1
        else:
            for j in range(1, b+1, 2):
                if ((i+j)%2) == 0: evPair += 1
    print(evPair)