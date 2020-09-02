# LeetCode Aug challenge 31

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root: return None
        if root.val < key: 
            root.right = self.deleteNode(root.right, key)
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:                                               # the node that neet to be deleted                
            if not root.left: return root.right
            
            if not root.right: return root.left

            if root.left and root.right:
                cur = root.right
                while cur.left: cur = cur.left
                root.val = cur.val
                root.right = self.deleteNode(root.right, root.val)
            
        return root
    
    # def printTree(self, root):
    #     q = []
    #     q.append(root)
    #     while(len(q)):
    #         cur = q[0]
    #         q.pop(0)

    #         vNodes = 0
    #         if cur.left: vNodes = 1, q.append(cur.left)
    #         if cur.right: vNodes = 1, q.append(cur.right)
    #         if vNodes: print(cur.val, end=' ')

            
'''Input:
    5
   / \
  3   6
 / \   \
2   4   7
Output:
    5
   / \
  4   6
 /     \
2       7
'''
if __name__ == '__main__': 
    root = TreeNode(5)  
    root.left = TreeNode(3)      
    root.right = TreeNode(6)  
    root.left.left = TreeNode(2)  
    root.left.right = TreeNode(4)  
    root.right.right = TreeNode(7)

    obj = Solution()
    roots = obj.deleteNode(root, 3)
    
    print(root.val, end=' ')
    print(root.left.val, end=' ')
    print(root.right.val, end=' ')
    print(root.left.left.val, end=' ')
    # print(root.left.right.val, end=' ')
    print(root.right.right.val, end=' ')

            
            
        