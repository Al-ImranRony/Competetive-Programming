# LeetCode Sept challenge 10

import sys
import math
import heapq      
import random
import collections
from collections import Counter, defaultdict

def getHint(secret, guess):
    bulls = sum([s == g for s, g in zip(secret, guess)])

    secretCnt = Counter(secret)
    guessCnt = Counter(guess)    
    guesses = sum([min(secretCnt[i], guessCnt[i]) for i in secretCnt])
    cows = guesses-bulls

    return f'{bulls}A{cows}B'

if __name__ == "__main__":
    print(getHint("1123", "0111"))
    print(getHint("1807", "7810"))