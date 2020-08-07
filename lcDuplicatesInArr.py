# LeetCode Aug challenge 06

import sys

sys.stdout = open("output.txt", "w")
sys.stdin = open("input.txt", "r")

lst = list(map(int, input().split()))
ans = []

seen = set()
for n in lst:
    if n in seen:
        ans.append(n)
    seen.add(n)

print(ans)            # All the elements that appear twice

        