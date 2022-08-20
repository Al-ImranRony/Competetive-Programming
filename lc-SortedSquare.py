


def sortedSquares(nums) -> list:
    start, end = 0, len(nums)-1 
    aos = [each**2 for each in nums]
    idx = end
    res = [0 for i in range(idx+1)] 

    while idx > -1:
        if aos[start]>aos[end]:
            res[idx] = aos[start]
            start+=1
        else:
            res[idx] = aos[end]
            end-=1
        idx-=1
        
    return res

print(sortedSquares([-4, -1, 0, 3, 10]))