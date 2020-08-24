# LeetCode Aug challenge 23

import sys
import math
import collections


class StreamChecker:
    def __init__(self, words):
        self.s = ''
        self.dict = collections.defaultdict(set)
        for word in words:
            self.dict[word[-1]].add(word)
        

    def query(self, letter: str) -> bool:
        self.s += letter
        return any(self.s.endswith(word) for word in self.dict[letter])

 
obj = StreamChecker(["cd","f","kl"])
param_1 = obj.query('a')
print(param_1)