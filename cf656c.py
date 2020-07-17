import sys

# sys.stdout = open("output.txt", "w")
# sys.stdin = open("input.txt", "r")

for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))

    if n<3 or sorted(l)==l:
        print(0)
        continue
    
    indx = ans = 0
    for i in range(n-2, -1, -1):
        if l[i+1] > l[i]:
            indx = i
            break
    for i in range(indx-1, -1, -1):
        if l[i] > l[i+1]:
            ans = i+1
            break
    
    print(ans)

