# LeetCode Aug challenge 08

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findPaths(self, root, target):
        if root:
            return int(root.val == target) + self.findPaths(root.left, target-root.val) + self.findPaths(root.right, target-root.val)
        return 0
    
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if root:
            return self.findPaths(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
        return 0

# obj = Solution()
