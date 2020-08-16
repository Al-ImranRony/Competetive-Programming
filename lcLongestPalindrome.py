# LeetCode Aug challenge 14

import collections

def longestPalindrome(s: str) -> int:
    occurance = collections.Counter(s)
    longPal = 0
    flagOdd = 0
    
    for k,v in occurance.items():            
        if v%2==0: 
            longPal += v
        else:    
            longPal += v-1
            flagOdd = 1
            
    return longPal if flagOdd==0 else (longPal + 1)

print(longestPalindrome("abccccdd"))