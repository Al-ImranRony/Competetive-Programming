# LeetCode Aug challenge 04

import sys

# sys.stdout = open("output.txt", "w")
# sys.stdin = open("input.txt", "r")

class Solution:
    def powerOfFour(self, n):
        if n < 1:
            return False
        while n%4 == 0:
            n = n / 4

        return n == 1

obj = Solution()
print(obj.powerOfFour(16))
print(obj.powerOfFour(5))