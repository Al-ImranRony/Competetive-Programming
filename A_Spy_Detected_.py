import sys
import math
import heapq 
import random
import collections
from collections import Counter, defaultdict, deque
from itertools import combinations, permutations


for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    for i in range(len(arr)):
        arr.count(arr[i])
        if arr.count(arr[i])==1:
            idx = i

    print(idx+1)

    