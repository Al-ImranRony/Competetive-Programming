# LeetCode Sept challenge 14

def rob(nums) -> int:
    if len(nums)==0: return 0        
    prev1 = prev2 = 0                 # Think of previous and 2nd previous house
    
    for n in nums:
        temp = prev1
        prev1 = max(prev2 + n, prev1) # Find max of previous house and 
        prev2 = temp                  # current + 2nd previous (non-adjacent) house
        
    return prev1

print(rob([2,0,0,2]))
print(rob([2,7,9,3,1]))