# Codechef easy practice

import sys
import math
import heapq 
import random
import collections
from collections import Counter, defaultdict
from itertools import combinations, permutations


for _ in range(int(input())):
    n = int(input())
    s = input()
    ones = s.count('1')
    print(ones + (ones*(ones-1)//2))
