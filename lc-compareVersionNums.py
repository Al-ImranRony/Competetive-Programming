# LeetCode Sept Challenge 09

def compVersion(version1, version2) -> int:
    v1, v2 = version1.split('.'), version2.split('.')
    length = max(len(v1), len(v2))

    for i in range(length):
        verNum1 = int(v1[i]) if i < len(v1) else 0 
        verNum2 = int(v2[i]) if i < len(v2) else 0 

        if verNum1 > verNum2: return 1
        elif verNum1 < verNum2: return -1
    return 0

print(compVersion("1.01", "1.001"))
print(compVersion("0.1", "1.1"))
print(compVersion("1.0.1", "1"))
