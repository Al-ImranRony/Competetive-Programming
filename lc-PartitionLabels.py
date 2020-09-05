# LeetCode Sept challenge day-4

import sys

def partisionLabels(s):
    parSizes, start, end = [], 0, 0

    last_seen = {char:i for i, char in enumerate(s)}  # Last index of every letter       
    for i, char in enumerate(s):
        end = max(end, last_seen[char])
        if i == end:
            parSizes.append(end+1 - start)            # Evaluate partision size by 
            start = i+1                               # partision start & end index

    return parSizes

print(partisionLabels("ababcbacadefegdehijhklij"))