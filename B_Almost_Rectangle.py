

import sys
import math
import heapq 
import random
import collections
from collections import Counter, defaultdict, deque
from itertools import combinations, permutations


for _ in range(int(input())):
    n = int(input())
    rows, cols = n, n
    arr = [[input() for i in range(cols)] for j in range(rows)]
    