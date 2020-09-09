# LeetCode Sept challenge 08

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumRootToLeaf(self, root: TreeNode, val=0) -> int:
        if not root: return 0
        
        val = val * 2 + root.val
        if (root.left == None) and (root.right == None): return val

        return self.sumRootToLeaf(root.left, val) + self.sumRootToLeaf(root.right, val)


'''
     1
   /  \
  0    1
 /\   /\
0  1 0  1
'''
treeChildsList = [1,0,1,0,1,0,1] 
if __name__ == '__main__': 
    root = TreeNode(1)  
    root.left = TreeNode(0)      
    root.right = TreeNode(1)  
    root.left.left = TreeNode(0)  
    root.left.right = TreeNode(1)
    root.right.left = TreeNode(0)  
    root.right.right = TreeNode(1)

    obj = Solution()
    print(obj.sumRootToLeaf(root))

