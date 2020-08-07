# LeetCode Aug challenge 02

import sys

# sys.stdout = open("output.txt", "w")
# sys.stdin = open("input.txt", "r")

class MyHashSet():
    def __init__(self):
        self.val = [False] * (1000000-1)

    def add(self, key):
        self.val[key] = True
    
    def remove(self, key):
        self.val[key] = False

    def contains(self, key):
        return self.val[key]


obj = MyHashSet()
obj.add(3)
print(obj.contains(3))
print(obj.contains(0))
obj.remove(3)
print(obj.contains(3))