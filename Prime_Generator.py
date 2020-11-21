# Day 14 of 100DaysOfCode

import sys
from math import sqrt
import heapq 
import random
import collections


for _ in range(int(input())):
    m, n = map(int, input().split())

    primes = {}
    for i in range(2, int(sqrt(n)+1)):
        for j in range(max(2, m//i), (n//i)+1):
            primes[i * j] = 1 

    for i in range(max(2, m), n+1):
        if i not in primes:
            print(i)
    print("")
