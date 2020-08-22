# LeetCode Aug challege 21

def sortArrayByParity(A):
        ans = []
        l = len(A)
        for i in range(l):
            if A[i]%2 == 0:
                ans.insert(0, A[i])
            else:
                ans.append(A[i])
        
        return ans

print(sortArrayByParity([1,1,0,1]))