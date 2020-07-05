import sys
from collections import deque

sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")


class Node:
    def __init__(self, data):
        self.left = self.right = None
        self.data = data


class Solution:
    def insert(self, root, data):
        if root is None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
            return root

    def levelOrder(self, root):
        if root is not None:
            queue = deque([root])
        else:
            queue = deque([])

        while queue:
            node = queue.popleft()
            print(node.data, end=" ")

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


t = int(input())
bst = Solution()
root = None
for i in range(t):
    data = int(input())
    root = bst.insert(root, data)
bst.levelOrder(root)

