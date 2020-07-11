import sys
import math

# sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")


def waterbombs(fire, w):
    c = b = 0
    for i in range(len(fire)):        
        if fire[i] == "x":
            c += 1
        if fire[i] == "Y":
            if c <= w and c != 0:
                b += 1
            else:
                b += math.ceil(c / w)
            c = 0
    if c>0:
        if c <= w and c != 0:
            b += 1
        else:
            b += math.ceil(c / w)
    return b

print(waterbombs("xxxxxYxxYYYxYxxxx", 3))