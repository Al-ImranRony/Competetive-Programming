# LeetCode Sept challenge 06

from collections import defaultdict, Counter


def imageOverlap(A, B):
    overlaps, lol, a, b = defaultdict(int), 0, [], []

    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j]==1: a.append((i, j))
            if B[i][j]==1: b.append((i, j))

    for p1 in a:
        for p2 in b:
            overlap = (p2[0]-p1[0], p2[1]-p1[1])
            overlaps[overlap] += 1
            lol = max(lol, overlaps[overlap])

    return lol

A = [[1,1,0],
     [0,1,0],
     [0,1,0]]
B = [[0,0,0],
     [0,1,1],
     [0,0,1]]
     
print(imageOverlap(A, B))

