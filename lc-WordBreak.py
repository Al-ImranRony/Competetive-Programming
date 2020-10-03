# LeetCode Sept Challenge 29

def wordBreak(s, wordDict) -> bool:
    n = len(s)
    dp = [i == 0 for i in range(n+1)]              # All elements are false except 1st one

    for i in range(n):
        if dp[i]:
            for j in range(i+1, n+1):
                if (s[i:j] in wordDict): dp[j] = True

    return dp[-1]


print(wordBreak("leetcode", ["leet", "code"]))
print(wordBreak("applepenapple", ["apple", "pen"]))
print(wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))