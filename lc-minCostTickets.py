# LeetCode Aug challenge 25

import sys
import math
import collections

class Solution:
    def mincostTickets(self, days, costs) -> int:
            lastDay = days[-1] + 1
            dp = [0] * lastDay

            days = set(days)

            for d in range(1, lastDay):
                if d in days:
                    dp[d] = min(costs[0]+dp[d-1], costs[1]+dp[max(d-7, 0)], costs[2]+dp[max(d-30, 0)])
                else: 
                    dp[d] = dp[d-1]
                # print(dp[d], '->', dp[d-1], dp[max(d-7, 0)], dp[max(d-30, 0)])

            return dp[-1]


if __name__ == '__main__': 
    obj = Solution()
    result = obj.mincostTickets([1,2,3,4,5,6,7,8,9,10,30,31], [2,7,15])
    print(result)