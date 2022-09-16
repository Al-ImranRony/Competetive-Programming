'''
First intuition solution, need too much time  O(n * log(n) * n), obvious TLE !
'''


def checkInclusion(s1, s2):
    res = False
    permutationS = []
    p = permute(s1, s2, "", permutationS)
    for each in p:
        if (each not in s2):
            res = False
        else:
            res = True
            break
    
    return res


def permute(s1, s2, ans, permutationS):
    ln = len(s1)
    alpha = [False] * 26
    
    if (ln == 0):
        permutationS.append(ans)
        print(ans, permutationS)

    for i in range(ln):
        char = s1[i]
        left, right = s1[0:i], s1[i+1: ]
        rest = left + right

        if (alpha[ord(char) - ord('a')] == False):
            permute(rest, s2, ans+char, permutationS)
        alpha[ord(char) - ord('a')] = True
    
    return permutationS


print(checkInclusion("aabc", "adkjhbaacwruy"))