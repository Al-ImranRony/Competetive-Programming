



def twoSum2(nums, target) -> list:
    ln, idx1 = len(nums), 0
    res = [] 
    while ln>0:
        diff = target - nums[idx1]
        s, e = idx1+1, len(nums)-1
        idx2 = binarySearch(nums, s, e, diff)

        if ( nums[idx2] == diff):
            res.append(idx1)
            res.append(idx2)
            return res
        else:
            idx1 += 1
            ln -= 1
    

def binarySearch(nums, start, end, x) -> int:
    low = start
    high = end
    mid = 0
 
    while low <= high:
        mid = (high + low) // 2

        # If x is greater, ignore left half
        if nums[mid] < x:
            low = mid + 1
        elif nums[mid] > x:
            high = mid - 1
        else:
            return mid

    return -1


print(twoSum2([2, 3, 4, 7, 11, 15], 15))