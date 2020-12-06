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
    num = [0]*(n+1)
    print(num, '*')
    for i in a:
        num[i] +=1
    print(num)
    if num.count(1)==0:
        print(-1)
    else:
        print(a.index(num.index(1))+1)
