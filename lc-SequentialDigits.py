# LeetCode Sept challenge 19

def sequentialDigits(low: int, high: int):
    nums = []
    for n in range(1,9):
        while n <= high:
            remainder = n % 10
            if remainder == 0: break
            if n >= low: nums.append(n)
            
            n = (n*10) + remainder + 1
        
    return sorted(nums)


print(sequentialDigits(100, 300))