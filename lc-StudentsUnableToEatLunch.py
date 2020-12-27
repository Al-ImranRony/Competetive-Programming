# 42th LeetCode Biweekly Contest

import sys
from collections import deque
from itertools import product


class Solution:
    def countStudents(self, students, sandwiches) -> int:
        gols, borgos = 0, 0
        for stu in students:
            if (stu == 0): gols += 1
            else: borgos += 1
        
        for i in range(len(sandwiches)):
            if (sandwiches[i] == 0): gols -= 1
            else: borgos -= 1
        
            if (gols < 0 or borgos < 0): return len(students)-i
        
        return 0

if __name__ == '__main__': 
    obj = Solution()
    res = obj.countStudents([1,1,1,0,0,1], [1,0,0,0,1,1])
    print(res)
