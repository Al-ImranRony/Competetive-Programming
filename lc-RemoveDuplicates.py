

def removeDuplicates(nums) -> list:
    s, besideS, e, k = 0, 1, len(nums)-1, 0
    ans = []
    while s<=e:
        if (s==e):
            k += 1
            ans.append(nums[s])
            s += 1
        else:
            if (nums[s]==nums[besideS]):
                s, besideS = s+1, besideS+1
            else:
                k += 1
                ans.append(nums[s])
                s, besideS = s+1, besideS+1    
    return ans

    # i = 0
    # while i < len(nums)-1:
    #     if (nums[i]==nums[i+1]):
    #         del nums[i]
    #     else:
    #         i += 1
                
    return len(nums)

print(removeDuplicates([1,1,2]))