# LeetCode Sept challenge 13


def insert(intervals, newInterval):
        s, e, res = newInterval[0], newInterval[1], []

        for i in intervals:
            if (i[1] < s) or (i[0] > e):
                res += [i]
            else:
                s, e = min(s, i[0]), max(e, i[1])

        res.append([s, e])
        return sorted(res)

print(insert([[1,3],[6,9]], [2,5]))
print(insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))
        