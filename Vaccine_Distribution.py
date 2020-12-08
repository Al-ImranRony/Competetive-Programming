# Codechef easy problem

import sys
import math
import heapq 
import random
import collections


for _ in range(int(input())):
    n, d = map(int, input().split())
    arr = list(map(int, input().split()))
    
    rp = nrp = ans = 0
    for i in arr:
        if (i <= 9 or i >= 80): rp += 1
        else: nrp += 1 
    
    ans = math.ceil(rp/d) + math.ceil(nrp/d)
    print(ans)
