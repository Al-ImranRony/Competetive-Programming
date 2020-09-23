# LeetCode Sept challenge 22

import sys
import math
import heapq 
import random
import collections
from collections import Counter, defaultdict
from itertools import combinations, permutations

# Need a O(n)time and O(1)space approach, but not this !
# def majorityElement(nums):
#         appearance, res = collections.Counter(nums), []
        
#         for n in appearance:
#             if (appearance[n] > len(nums)/3): res.append(n)
                
#         return res

# Time: O(n), Space: O(1)
def majorityElement(nums):
    appears = Counter()
    for n in nums:
        appears[n] += 1
        if len(appears) == 3:
            appears -= Counter(set(appears))       # Deducted 1 set of keys from appears

    return [n for n in appears if (nums.count(n) > len(nums)/3)]



print(majorityElement([2,2,1,3]))
print(majorityElement([1,1,1,3,3,2,2,2]))