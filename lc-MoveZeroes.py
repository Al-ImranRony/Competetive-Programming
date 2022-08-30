'''
Leetcode daily challenge: Move Zeroes
In-place array ellement modification, using 2-pointer approach !
'''

def singleSwap(nums, start, end):
        temp = nums[start]
        nums[start] = nums[end]
        nums[end] = temp 
        start += 1
        end -= 1

def moveZeroes(nums) -> list:

    left, right, willSwap = 0, 1, False

    while True:
        if right >= len(nums):
            break

        if (nums[left]==0):
            willSwap = True
        else:
            willSwap = False
        if (nums[right]==0):
            if willSwap:
                right += 1
            else:
                left = right
                right += 1
        else:
            if willSwap:
                singleSwap(nums, left, right)
                left += 1
                right += 1
            else:
                left += 2
                right += 2

    return nums

print(moveZeroes([0, 1, 0, 3, 12]))