# Codeforces round 677-A

for _ in range(int(input())):
    x = input()
    n, ans = len(x), 0
    while n:
        ans += n
        n -= 1
    x = int(x[0])
    ans += (x-1)*10
    print(ans)