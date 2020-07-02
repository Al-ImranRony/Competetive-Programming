import sys

sys.stdin  = open("input.txt", "r")
sys.stdout  = open("output.txt", "w")


for _ in range(int(input())):
    n, r = map(int, input().split())
    r = min(n,r)
    if n>r:
        print((r*(r+1))//2)            
    else:
        print(((r*(r-1))//2)+1)