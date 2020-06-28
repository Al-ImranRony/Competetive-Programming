import sys

sys.stdout = open("output.txt", "w")
sys.stdin = open("input.txt", "r")


for t in range(int(input())):
    x, y, n = map(int, input().split())
    p = n%x
    if p == y:
        print(n)
    elif p > y:
        print(n-p+y)
    else:
        print(n-x-p+y)

