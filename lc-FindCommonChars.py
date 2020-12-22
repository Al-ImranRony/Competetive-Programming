# LeetCode easy problem, QuickFind-UnionFind problems
# Time - O(n*n)

import sys
import math
import heapq 
import random
import collections
from collections import Counter, defaultdict
from itertools import combinations, permutations


class Solution:
    def commonChars(self, a):
        if len(a) < 2: return a

        res, fword = [], set(a[0])       
        for char in fword:
            charFreq = min([word.count(char) for word in a])

            if charFreq: res += [char]*charFreq

        return res


if __name__ == "__main__":
    obj = Solution()
    result = obj.commonChars(["cool","lock","cook"])
    print(result)