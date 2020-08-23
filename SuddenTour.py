import sys
import math

# sys.stdin = open("input.txt", "r")
# sys.stdout = open("output.txt", "w")

for case in range(int(input())):
    def knapSack(W, wt, val, n):
        K = [[0 for x in range(W + 1)] for x in range(n + 1)] 
  
        for i in range(n + 1): 
            for w in range(W + 1): 
                if i == 0 or w == 0: 
                    K[i][w] = 0
                elif wt[i-1] <= w: 
                    K[i][w] = max(val[i-1]+ K[i-1][w-wt[i-1]],  K[i-1][w]) 
                else: 
                    K[i][w] = K[i-1][w] 
    
        return K[n][W]

    nc = list(map(int, input().split()))
    n, c = nc[0], nc[1]
    w, val = [], []
    for i in range(n):
        sifi = list(map(int, input().split()))
        w.append(sifi[0])
        val.append(sifi[1])

    fv = knapSack(c, w, val, n)
    print("Case {}: {}".format(case+1, fv))

    


