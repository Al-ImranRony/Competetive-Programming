import sys

# sys.stdout = open("june16/output.txt", "w")
# sys.stdin = open("june16/input.txt", "r")

for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    odd, even = 0, 0
    for i in range(n):
        if i % 2 != a[i] % 2:
            if a[i] % 2:
                even += 1
            else:
                odd += 1
    if odd != even:
        print(-1)
    else:
        print(odd)
