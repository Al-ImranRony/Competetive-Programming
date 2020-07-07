import sys
import math

sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")

da, ma, ya = map(int, input().split())
de, me, ye = map(int, input().split())

sum = 0

if (ye < ya):
    sum += 10000
elif (ye == ya):
    if (me < ma):
        sum += (ma-me)*500
    elif (me == ma):
        if (de < da):
            sum += (da-de)*15

print(sum)