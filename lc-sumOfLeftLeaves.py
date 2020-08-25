# LeetCode Aug challenge 24

import sys
import math
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        sum = 0 
        stack = [(root, True)]
        
        while stack:
            node, is_empty = stack.pop()
            if (not node.left and not node.right) and not is_empty:
                sum += node.val
                continue
            if node.left:
                stack.append((node.left, False))
            if node.right:
                stack.append((node.right, True))
	
        return sum


treeChildsList = [3,9,20,None,None,15,7] 
if __name__ == '__main__': 
    root = TreeNode(3)  
    root.left = TreeNode(9)      
    root.right = TreeNode(20)  
    root.right.left = TreeNode(15)  
    root.right.right = TreeNode(7)

    obj = Solution()
    print(obj.sumOfLeftLeaves(root))
