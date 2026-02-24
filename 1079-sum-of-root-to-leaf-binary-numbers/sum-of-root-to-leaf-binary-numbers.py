# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        total = 0

        def traverse(node, current):
            if node is None:
                return
            
            current = current * 2 + node.val
            if node.left is None and node.right is None:
                nonlocal total
                total += current
                return

            traverse (node.left, current)
            traverse (node.right, current)
        
        traverse (root, 0)
        return total



        