# LeetCode Aug challenge 11

def hIndex(citations):
    if len(citations) == 0:
            return 0
        
    citations.sort(reverse = True)    
    if citations[-1] >= len(citations):
        return len(citations)
    
    res = 0
    for i in range(len(citations)):
        if i >= citations[i]:
            res = i
            break
    return res

print(hIndex([3,0,6,1,5]))