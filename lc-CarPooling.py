# LeetCode Sept challenge 21

import sys
import math
import heapq 
import random
import collections
from collections import Counter, defaultdict
from itertools import combinations, permutations


def carPooling(trips, capacity: int) -> bool:
    events, passengers = Counter(), 0

    for n, pick, drop in trips:
        events[pick] += n
        events[drop] -= n

    for km in sorted(events):   
        passengers += events[km]
        if passengers > capacity: return False

    return True


print(carPooling([[2,1,5],[3,3,7]], 4))
print(carPooling([[2,1,5],[3,5,7]], 3))
print(carPooling([[3,2,7],[3,7,9],[8,3,9]], 11))
print(carPooling([[3,2,7],[1,7,9],[8,3,9]], 10))
