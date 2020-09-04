# LeetCode Sept challenge day-3

def repeatedSubstringPattern(s: str) -> bool:
    return s in (s[1:]+s[:-1])

print(repeatedSubstringPattern("abcabcabcabc"))
print(repeatedSubstringPattern("aba"))