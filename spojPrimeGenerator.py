import sys
from math import sqrt

sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")

# By brute force
for _ in range(int(input())):
    m, n = map(int, input().split())
    primes = {}
    for i in range(2, int(sqrt(n)+1)):
        for j in range(max(m//i, 2), (n//i)+1):
            primes[i * j] = 1

    for i in range(max(m, 2), n+1):
        if i not in primes:
            print(i) 

    

