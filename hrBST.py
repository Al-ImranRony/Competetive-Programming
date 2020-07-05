import sys

sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")

class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data

class Solution:
    # TODO: Making BS tree by insert method
    def insert(self, root, data):
        if root is None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)   #Recursion
                root.left = cur
            else:
                cur = self.insert(root.right, data)  
                root.right = cur
            return root

    def getHeight(self, root):
        if root is None:
            return -1
        else:
            rh = self.getHeight(root.right)
            lh = self.getHeight(root.left)
            return (1 + max(rh, lh))        

t=int(input())
bst=Solution()
root=None
for i in range(t):
    data=int(input())
    root=bst.insert(root,data)
height=bst.getHeight(root)
print(height)       