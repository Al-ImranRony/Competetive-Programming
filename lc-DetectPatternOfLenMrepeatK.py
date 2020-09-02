import sys
import math
import heapq      
import random
import collections
from collections import Counter, defaultdict

def containsPattern(arr, m: int, k: int) -> bool:
    i = 0
    while i <= (len(arr)-1):
        p = arr[i:i+m]
        if p*k == arr[i:i+m*k]:
            return True
        i += 1
        
    return False

print(containsPattern([1,2,1,2,1,1,1,3], 2, 2))