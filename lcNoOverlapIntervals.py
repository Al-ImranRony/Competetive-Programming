# LeetCode Aug challenge 15

def eraseOverlapIntervals(intervals):
    intervals.sort()
    prev = float("-inf")
    res = 0

    for i in intervals:
        if i[0] >= prev:
            prev = i[1]
        else: 
            res += 1
            prev = min(prev, i[1])

    return res

lst = [[1,2],[1,2],[1,2]]
print(eraseOverlapIntervals(lst))
