import sys
from collections import deque

sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")


class AdvancedArithmetic(object):      # <- Interface
    @staticmethod
    def divisorSum(n):  
        raise NotImplementedError 


class Calculator(AdvancedArithmetic): 
    def divisorSum(self, n):           # <- Abstract method
        sum = 0
        for i in range(1, n + 1):
            if n % i == 0:
                sum += i
        return sum


n = int(input())
my_calculator = Calculator()

s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)
