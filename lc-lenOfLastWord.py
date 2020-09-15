# LeetCode Sept challenge 15

def lengthOfLastWord(s: str) -> int:     
    words = s.split()  
    if words: return len(words[-1])
    return 0


print(lengthOfLastWord("Hello World"))
print(lengthOfLastWord(" "))
print(lengthOfLastWord("a "))