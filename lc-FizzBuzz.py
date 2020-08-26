# LeetCode Aug challenge 26

import sys
import math
import heapq        # helps to return the top n smallest/largest elems
import collections
from collections import Counter, defaultdict
     

class Solution:
    def fizzBuzz(self, n):
        return ["FizzBuzz" if i%15==0 else "Buzz" if i%5==0 else "Fizz" if i%3==0 else str(i) for i in range(1, n+1)]

if __name__ == '__main__': 
    obj = Solution()
    result = obj.fizzBuzz(15)
    print(result)

