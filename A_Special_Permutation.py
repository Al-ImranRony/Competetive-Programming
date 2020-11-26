# Codeforces Round 686, Div3 - a

from itertools import combinations, permutations


for _ in range(int(input())):
    n = int(input())

    print(set(permutations(n)))
    print("")