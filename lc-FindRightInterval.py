# LeetCode Aug challenge 27

import sys
import math
import heapq     
import random
import collections
from collections import Counter, defaultdict

def findRightInterval(intervals):
    ints = sorted([[j,k,i] for i,[j,k] in enumerate(intervals)])
        begs = [i for i,_,_ in ints]
        out = [-1]*len(begs)
        for i,j,k in ints:
            t = bisect.bisect_left(begs, j)
            if t < len(begs):
                out[k] = ints[t][2]
        
        return out


ans = findRightInterval([ [3,4], [2,3], [1,2] ])
print(ans)