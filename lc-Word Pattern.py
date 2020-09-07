# LeetCode Sept challenge 07

from collections import defaultdict, Counter

def wordPattern(pattern, str):
    words, pat = str.split(), pattern
    
    # length of pattern & length words of the str must be same !
    if len(pat) != len(words): return False    
    else: return len(set(zip(pat, words))) == len(set(pat)) == len(set(words))

print(wordPattern("abba", "dog cat cat dog"))
print(wordPattern("abba", "dog cat cat fish"))
print(wordPattern("aaaa", "dog cat cat dog"))
print(wordPattern("abba", "dog dog dog dog"))