# LeetCode Aug challenge 28

import random


def rand7():
    n = random.randint(1, 7)
    return n

# Implement Rand10() Using Rand7(), minimize the number of calls to rand7()
def rand10():                               
    while True:                             
        num = (rand7()-1) * 7 + rand7()

        if num <= 40:
            return num % 10 + 1


if __name__ == '__main__': 
    res = []
    for i in range(int(input())):
        res.append(rand10())

    print(res)