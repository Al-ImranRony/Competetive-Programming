# LeetCode Sept Challenge 28

def numSubarrayProductLessThanK(nums, k: int) -> int:
    product, leftmost, count = 1, 0, 0

    for cur in range(len(nums)):
        product *= nums[cur]
        while (product >= k) and (leftmost <= cur):
            product /= nums[leftmost]
            leftmost += 1
        count += cur - leftmost + 1
        
    return count


print(numSubarrayProductLessThanK([10, 5, 2, 6], 100)) 
print(numSubarrayProductLessThanK([10, 5, 2, 6, 9], 200)) 