import sys

sys.stdout = open("output.txt", "w")
sys.stdin = open("input.txt", "r")

for _ in range(int(input())):
    l = list(map(int, input().split()))
    l.sort()
    if l[0]==l[1]==l[2]:
        print("YES")
        print(*l)
    elif l[1]==l[2]:
        print("YES")
        print(l[0], l[1], l[0])
    else: 
        print("NO")



    