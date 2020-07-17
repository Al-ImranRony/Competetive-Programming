import sys

# sys.stdin = open("input.txt", "r")
# sys.stdout = open("output.txt", "w")

for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    a = [l[0]]
    for i in range(1, len(l)-1):
        if l[i] not in a:
            a.append(l[i])
    for i in range(n):
        print(a[i], end=' ')
    print('')


