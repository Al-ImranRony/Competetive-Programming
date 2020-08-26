# My template for CP

import sys
import math
import heapq        # helps to return the top n smallest/largest elems
import collections
from collections import Counter, defaultdict

     
for _ in range(int(input())):
    x, y, k, n = map(int, input().split())

    
class Solution:
    def func(self, x, n):
        return x

if __name__ == '__main__': 
    obj = Solution()
    result = obj.func([1,2,3,4,5,6,7,8,9], [2,3,6])
    print(result)

zipped = zip(dict.values(), dict.keys())
print(sorted(zipped))                             # sorted by values 