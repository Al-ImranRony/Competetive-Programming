



def permute(s1, s2, ans):
    ln = len(s1)
    alpha = [False] * 26
    res = False

    if (ln == 0):
        print(ans, end = " ")
        if (ans not in s2):
            res = False
        else:
            return True
        return res

    for i in range(len(s1)):
        char = s1[i]
        left, right = s1[0:i], s1[i+1: ]
        rest = left + right

        if (alpha[ord(char) - ord('a')] == False):
            permute(rest, s2, ans+char)
        alpha[ord(char) - ord('a')] = True
        # permute(rest, s2, ans+char)


print(permute("aabc", "adkjhbaacwruy", ""))
# permute("aabc", "adkjhbaacwruy", "")