import sys
import math

sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")


n = int(input())
lines = sys.stdin.readlines()       # Prompt for several lines (of input)
ll = []
for line in lines:
    mail = line.strip()
    if mail.endswith("@gmail.com"):
        name = mail.split(" ")[0]
        ll.append(name)
nl = sorted(ll)
for i in range(len(nl)):
    print(nl[i])

    