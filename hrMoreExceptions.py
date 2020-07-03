import sys

sys.stdin  = open("input.txt", "r")
sys.stdout  = open("output.txt", "w")

class Calculator:
    def power(self, n, p):        
        if (n<0) or (p<0):
            raise Exception("n and p should be non-negative")
        else:
            return pow(n, p)

mycalculator = Calculator()
for _ in range(int(input())):
    n, p = map(int, input().split())
    try:
        ans = mycalculator.power(n, p)
        print(ans)
    except Exception as e:
        print(e)
