


def rotateArray(nums, k) -> list:
    ln, k = len(nums), (k % len(nums))
    
    reverse(nums, 0, ln-1)
    reverse(nums, 0, k-1)
    reverse(nums, k, ln-1)
    
    return nums

def reverse(nums, start, end):
    while start < end: 
        temp = nums[start]
        nums[start] = nums[end]
        nums[end] = temp 
        start += 1
        end -= 1


print(rotateArray([1, 2, 3, 4, 5, 6, 7], 3))

# while lan>0:
#     # print(lan)
#     ans.append(nums[l])
#     l += 1
#     lan -= 1
# while ran>0:
#     ans.append(nums[r])
#     r += 1
#     ran -= 1