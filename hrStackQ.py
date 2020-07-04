import sys
from collections import deque

sys.stdin  = open("input.txt", "r")
sys.stdout  = open("output.txt", "w")

class Solution:
    def __init__(self):
        self.stack = []
        self.queue = deque([])
    def pushCharacter(self, pc):
        self.stack.append(pc)
    def enqueueCharacter(self, ec):
        self.queue.append(ec)
    def popCharacter(self):
        return self.stack.pop()
    def dequeueCharacter(self):
        return self.queue.popleft()

s = input()
l = len(s)

#Create the Solution class object
obj=Solution()   

# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break

if isPalindrome:
    print("The word,"+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.") 