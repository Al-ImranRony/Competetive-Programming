# Day 5 of 100daysCodingChallenge; Uber coding interview problem

import sys
import math
import heapq 
import random
import collections
from collections import Counter, defaultdict
from itertools import combinations, permutations

arr = [1, 2, 3, 4, 5]
totalProduct = math.prod(arr)
ans = [totalProduct//i for i in arr]
print(ans)

#Try it without dividing !
