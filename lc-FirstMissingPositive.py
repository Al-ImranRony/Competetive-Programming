# LeetCode Sept challenge 30

def firstMissingPositive(nums) -> int:
    for i in range(len(nums)):
        if 0 <= nums[i]-1 < len(nums) and (nums[nums[i]-1] != nums[i]):
            temp = nums[i] - 1
            nums[i], nums[temp] = nums[temp], nums[i]

    for i in range(len(nums)):
        if nums[i] != i+1:
            return i+1
    return len(nums)+1

print(firstMissingPositive([1,2,0]))
print(firstMissingPositive([3,4,-1,1]))
print(firstMissingPositive([7,8,9,11,12]))