# LeetCode Sept challenge 05


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getAllElements(self, root1:TreeNode, root2:TreeNode):
        res = []
        def inorder(root):
            if root:
                inorder(root.left)
                res.append(root.val)
                inorder(root.right)
            else:
                return None

        inorder(root1)
        inorder(root2)

        return sorted(res)

'''Input:
    2      1
   / \    / \
  1   4  0   3
'''


if __name__ == '__main__': 
    root1 = TreeNode(2)  
    root1.left = TreeNode(1)      
    root1.right = TreeNode(4)  
    root2 = TreeNode(1)  
    root2.left = TreeNode(0)  
    root2.right = TreeNode(3)

    obj = Solution()
    result = obj.getAllElements(root1, root2)
    print(result)

    