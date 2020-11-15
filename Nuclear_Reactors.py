# Codechef easy problem 


a, n, k = map(int, input().split())
p = n+1
for i in range(k):
    print(a % p, end=" ")
    a = a // p
        
