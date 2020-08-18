# LeetCode Aug challenge 17

def distributeCandies(candies, n):
    res = [0] * n
    c = 0
    while candies > 0:
        res[c%n] += min(candies, c+1)
        c += 1
        candies -= c
    return res

print(distributeCandies(10, 3))
