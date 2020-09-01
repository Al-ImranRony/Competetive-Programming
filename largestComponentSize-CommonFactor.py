# LeetCode Aug challenge 30

import math
from collections import defaultdict, Counter

class DisjSet:
    def __init__(self, N):
        self.parent = list(range(N))
    
    def find(self, x):                               # Finding till parent node
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):                           # Point y to x(parent) to union 
        xn, yn = self.find(x), self.find(y)
        self.parent[xn] = yn

class Solution:
    def primes_set(self, n):                         # Generate set of primes for number n                        
        for i in range(2, int(math.sqrt(n))+1):
            if n%i == 0:
                return self.primes_set(n//i) | set([i])

        return set([n])

    def largestComponentSize(self, A):
        n = len(A)
        UF = DisjSet(n)
        primes = defaultdict(list)
    
        for i, num in enumerate(A):                  # Calculate primes set for all elements in A
            pr_set = self.primes_set(num)
            for q in pr_set: primes[q].append(i)
	
        for _, indexes in primes.items():            # Union disjoin set based on same prime
            for i in range(len(indexes)-1):
                UF.union(indexes[i], indexes[i+1])
		
        return max(Counter([UF.find(i) for i in range(n)]).values())


if __name__ == '__main__': 
    obj = Solution()
    result = obj.largestComponentSize([2,3,6,7,4,12,21,39])
    print(result)
