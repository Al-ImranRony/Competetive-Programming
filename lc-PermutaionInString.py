'''
First intuition solution, need too much time  O(n * log(n) * n), obvious TLE !
'''

from collections import Counter

def checkInclusion(s1, s2):
    ln1, ln2 = len(s1), len(s2)
    s1CharFreq = Counter(s1)

    for i in range(ln2):
        window = s2[i: i+ln1]
        s2WindowFreq = Counter(window)

        if (s1CharFreq == s2WindowFreq):
            return True
        
    return False
    