# LeetCode Aug challenge 12

import sys

# sys.stdout = open("output.txt", "w")
# sys.stdin = open("input.txt", "r")

class Solution:
    def getRow(self, rowIndex: int):
        n = 1
        res = [n]
        for i in range(rowIndex):
            n = int(n * (rowIndex-i)/(i+1))
            res.append(n)
        return res

obj = Solution()
pn = input()
ans = obj.getRow(int(pn))
print(ans)