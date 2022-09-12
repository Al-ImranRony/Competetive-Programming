


def lengthOfLongestSubstring(s):  
    left = right = 0
    lsl, ln = 0, len(s)
    window = set()

    while left < ln and right < ln:
        if (s[right] not in window):
            if right+1 < ln: 
                window.add(s[right])
            right += 1
            lsl = max(lsl, right-left)
        else:
            window.remove(s[left])
            left += 1

        
    return lsl


print(lengthOfLongestSubstring("dvdf"))
# print(lengthOfLongestSubstring("wwwww"))
# print(lengthOfLongestSubstring("asdghjl;bxzr;tyu"))