# LeetCode Aug challenge 01

import sys

# sys.stdout = open("output.txt", "w")
# sys.stdin = open("input.txt", "r")


def detectCapitalUse(word: str):
    return word.isupper() or word.istitle() or word.islower()

print(detectCapitalUse("USA"))