# LeetCode Sept challenge 30

def firstMissingPositive(nums) -> int:
    pIn = {}
    for n in nums:
        if n > 0: pIn[n] = 1            # Create a dict of positive ints only
        
    if not pIn: return 1                # Check if all the nums were negative
    
    pInList = sorted(list(pIn.keys()))  # Remove duplicates with sorting the keys of dict
    
    for i in range(1, len(pIn)+1):
        if i < pInList[i-1]: return i   # Check if any number missing             
    return  len(pIn)+1

    # for i in range(len(nums)):
    #     while 0 <= nums[i]-1 < len(nums) and (nums[nums[i]-1] != nums[i]):
    #         tmp = nums[i]-1
    #         nums[i], nums[tmp] = nums[tmp], nums[i]

    # for i in range(len(nums)):
    #     if (nums[i] != i+1): return i+1
    # return len(nums)+1

print(firstMissingPositive([1,2,0]))
print(firstMissingPositive([3,4,-1,1]))
print(firstMissingPositive([7,8,9,11,12]))