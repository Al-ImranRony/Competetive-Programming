# LeetCode Aug challenge 27

import sys
import math
import heapq     
import bisect
import collections
from collections import Counter, defaultdict

def findRightInterval(intervals):
    ints = sorted([[i,j,k] for k,[i,j] in enumerate(intervals)])  # Sorted by j (k->index)
    startps = [i for i,_,_ in ints]
    res = [-1]*len(startps)

    for _,j,k in ints:
        t = bisect.bisect_left(startps, j)
        if t < len(startps):
            res[k] = ints[t][2]
    
    return res


ans = findRightInterval([[1,4], [2,3], [3,4]])
print(ans)