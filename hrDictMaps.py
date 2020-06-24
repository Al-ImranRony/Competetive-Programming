import sys

# sys.stdin = open("input.txt", "r")
# sys.stdout = open("output.txt", "w")

n = int(input())
Cntcts = dict()
for i in range(n):
    a, b = input().split()
    Cntcts[a] = b

lines = sys.stdin.readlines()
for line in lines:
    q = line.strip()
    if q in Cntcts:
        print(q + "=" + Cntcts[q])
    else:
        print("Not found")
