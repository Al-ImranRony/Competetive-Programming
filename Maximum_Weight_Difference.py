# Codechef easy practice

for _ in range(int(input())):
    n, k = map(int, input().split())
    w = list(map(int, input().split()))
    son, chef = 0, 0
    for i in sorted(w):
        if k>0:
            son += i
            k -= 1
        else:
            chef += i
    print(chef-son)

