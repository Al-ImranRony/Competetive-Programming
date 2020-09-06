# LeetCode Sept challenge day-2

import sys
from sortedcontainers import SortedList                        


def containsNearbyAlmostDuplicate(nums, k: int, t: int) -> bool:
    sList = SortedList()
    for i in range(len(nums)):
        if i > k: sList.remove(nums[i - k-1])
   
        posA = sList.bisect_left(nums[i] - t)
        posB = sList.bisect_right(nums[i] + t)
        if (posA != posB) and (posA != len(sList)):
            return True
        
        sList.add(nums[i])
        
    return False

print(containsNearbyAlmostDuplicate([1,2,3,1], 3, 0))
        