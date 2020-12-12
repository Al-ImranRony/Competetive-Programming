# Codechef dec challenge - 1

import sys
import math
import heapq 
import random
import collections


d1, v1, d2, v2, p = map(int, input().split())
vacPro, d = 0, 0
while (vacPro < p):
    d += 1
    if (d >= d1): vacPro += v1
    if (d >= d2): vacPro += v2
    
print(d)

