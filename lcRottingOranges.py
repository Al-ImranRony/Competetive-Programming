# LeetCode Aug challenge 09

import sys
from collections import deque
from itertools import product


# sys.stdout = open("output.txt", "w")
# sys.stdin = open("input.txt", "r")

class Solution:
    def orangesRotting(self, grid):
        m, n, queue, freshOrng = len(grid), len(grid[0]), deque(), 0
        for i, j in product(range(m), range(n)):
            if grid[i][j] == 2: queue.append((i, j))
            if grid[i][j] == 1: freshOrng += 1
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        minits = 0

        while queue:
            minits += 1
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in directions:
                    if (0<=x+dx<m) and (0<=y+dy<n) and grid[x+dx][y+dy] == 1:
                        freshOrng -= 1
                        grid[x+dx][y+dy] = 2
                        queue.append((x+dx, y+dy))

        return -1 if freshOrng != 0 else max(minits-1, 0)


if __name__ == '__main__': 
    grid = [[2, 1, 1], 
        [0, 1, 1], 
        [1, 0, 1]] 

    obj = Solution()
    res = obj.orangesRotting(grid)
    print(res)




