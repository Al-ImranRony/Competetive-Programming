# LeetCode Aug challenge 10

import sys

sys.stdout = open("output.txt", "w")
sys.stdin = open("input.txt", "r")

class Solution:
    def titleToNumber(self, s: str) -> int:
        result = 0
        for c in range(len(s)):  
            result *= 26 
            result += ord(s[c]) - ord('A') + 1   # Converted to unicode to calculate
        print(result)
        return result

obj = Solution()
stng = input()
column = obj.titleToNumber(stng)
print(column)
