
for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    print(min(abs(a[i]-a[i+1]) for i in range(0, n-1)))