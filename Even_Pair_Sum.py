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
    aEven = a//2
    aOdd= a-aEven
    bEven = b//2
    bOdd = b-bEven
    print(aEven*bEven + aOdd*bOdd)