# Codechef easy practice

for _ in range(int(input())):
    n, k = map(int, input().split())
    w = list(map(int, input().split()))
    w.sort()
    if k <= n//2:
        items = k
    else:
        items = n-k

    w1, w2 = w[0:items], w[items:n]
    s1, s2 = sum(w1), sum(w2)
    print(s2-s1)

