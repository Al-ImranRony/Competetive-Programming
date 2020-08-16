# LeetCode Aug challenge 13

from itertools import combinations 

class CombinationIterator:

    def __init__(self, chars: str, combLength: int):
        self.allCombinations = list(combinations(chars, combLength))
        self.count = 0

    def next(self) -> str:
        self.count += 1
        return "".join(self.allCombinations[self.count-1])
        
    def hasNext(self) -> bool:
        return self.count < len(self.allCombinations)
        


obj = CombinationIterator("abc", 2)
print(obj.next())
print(obj.hasNext())
