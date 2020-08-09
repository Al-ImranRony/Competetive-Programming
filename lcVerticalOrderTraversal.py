# LeetCode Aug challenge 07

import sys
import collections

# sys.stdout = open("output.txt", "w")
# sys.stdin = open("input.txt", "r")

class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = self.right = None


def verticalTraversal(root: TreeNode):
    x_axis = collections.defaultdict(list)
    def dfs(node, x=0, y=0):
        if not node: return None
        x_axis[x].append([y, node.val])

        dfs(node.left, x-1, y+1)
        dfs(node.right, x+1, y+1)

    dfs(root)
    res = []
    items = list(x_axis.items())
    items.sort()

    for k, v in items:
        v.sort()
        item = list(x[1] for x in v)
        res.append(item)
        
    return res

if __name__ == "__main__":

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    print(verticalTraversal(root))
    
    