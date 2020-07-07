import sys
import math

sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")


def CheckPrime(n, c):
    # It checks the primality in the worst case scenario
    if n == 2:
        c += 1
        print("Prime", "-> Iterration needed:", c)
        return
    if n == 1 or n % 2 == 0:
        c += 1
        print("Not prime", "-> Iterration needed:", c)
        return

    sr = int(math.sqrt(n))

    for i in range(3, sr + 1, 2):
        c += 1
        if n % i == 0:
            print("Not prime", "-> Iterration needed:", c)

    print("Prime", "-> Iterration needed:", c)


for _ in range(int(input())):
    n = int(input())
    c = 0
    CheckPrime(n, c)

    