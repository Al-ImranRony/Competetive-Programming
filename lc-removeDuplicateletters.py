# LeetCode Oct Challenge 11
# Problem Similarities: Smallest Subsequence of Distinct Characters

def removeDuplicateLetters(s) -> str:
    lastIdxs = {ltr: idx for idx, ltr in enumerate(s)}
    stack = []

    for i, ltr in enumerate(s):
        if ltr in stack: continue
        while stack and (ltr < stack[-1]) and (i < lastIdxs[stack[-1]]):  
            stack.pop()
        stack.append(ltr)

    return ''.join(stack)


print(removeDuplicateLetters("cbacdcbc"))
print(removeDuplicateLetters("bcabc"))
print(removeDuplicateLetters("bcghfjgabc"))

