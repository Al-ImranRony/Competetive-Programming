import sys

sys.stdout = open("output.txt", "w")
sys.stdin = open("input.txt", "r")


class Difference:
    maxm = 0
    minm = 100

    def __init__(self, a):
        self.elements = a

    def computeDifference(self):
        sEl = sorted(self.elements)
        self.maxDiff = abs(sEl[-1]-sEl[0])


n = int(input())
a = [int(e) for e in input().split(" ")]

d = Difference(a)
d.computeDifference()
print(d.maxDiff)
