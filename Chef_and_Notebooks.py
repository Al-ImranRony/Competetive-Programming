# First CodeChef solution

import sys
import math
import heapq        
import collections
from collections import Counter, defaultdict

for _ in range(int(input())):
    flg = False
    x, y, k, n = map(int, input().split())
    for i in range(n):
        pages, price = map(int, input().split())
        if (x-y <= pages) and (price <= k):
            flg = True

    if flg: print("LuckyChef")
    else: print("UnluckyChef")