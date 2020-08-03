# LeetCode Aug challenge 03

import sys

# sys.stdout = open("output.txt", "w")
# sys.stdin = open("input.txt", "r")


def isPalindrome(s):
    return s == s[::-1]


si = input()
s = ""
for i in range(len(si)):
    if si[i].isalnum():
        s += si[i].lower()
if isPalindrome(s):
    print("true")
else:
    print("false")
