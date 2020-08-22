import sys
import math

# sys.stdin = open("input.txt", "r")
# sys.stdout = open("output.txt", "w")

n = input()
l = len(n)
m = ['m','i','c','r','o','s','f','t']

for i in range(l):
    if n[i] in m:
        m.remove(n[i])
    if m is None: break
    
if m:
    print("Only I love Microsoft!")
else:
    print("We both love Microsoft!")