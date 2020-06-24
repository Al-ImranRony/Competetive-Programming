import sys

# sys.stdout = open("output.txt", "w")
# sys.stdin = open("input.txt", "r")

t = int(input())
for j in range(t):
    s = input()
    if len(s) > 2:
        sa = s[0] + s[1]
        for i in range(2, len(s)):
            if i % 2 == 0:
                continue
            else:
                sa = sa + s[i]
        print(sa)
    else:
        print(s)
