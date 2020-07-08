import math
import os
import random
import re
import sys


sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")

# Ex: a=1, b=2 => a=00ol so, a&b=> 0001
#                 b=00ll
# x << y - Returns x with bits shifted to left by y places (and new bits on rightside are zeros). This is the same as multiplying x by 2**y.
# x >> y - Returns x with bits shifted to right by y places. This is the same as dividing(//) x by 2**y.
# x & y - "bitwise AND". Each bit of the output is 1 if the corresponding bit of x and y is 1, otherwise it's 0.
# x | y - "bitwise OR". Each bit of the output is 0 if the corresponding bit of x and y is 0, otherwise it's 1.
# ~ x   - Returns the complement of x - the number you get by switching each 1 for a 0 and each 0 for a 1. This is the same as -x - 1.
# x ^ y - "bitwise exclusive or". Each bit of the output is the same as the corresponding bit in x if that bit in y is 0, and it's the complement of the bit in x if that bit in y is 1.


# BruteForce - TimeLimit exceed

# for _ in range(int(input())):
#     mpv, v = 0, 0
#     n, k = map(int, input().split())
#     for i in range(1, n+1):
#         for j in range(2, n+1):
#             if (i&j < k):
#                 v = i&j
#                 if v > mpv:
#                     mpv = v
#     print(mpv)

for _ in range(int(input())):
    n, k = map(int, input().split())
    print(k - 1 if ((k - 1) | k) <= n else k - 2)

