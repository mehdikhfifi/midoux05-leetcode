# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        res = 0
        def explore(node):
            nonlocal res
            if not node:
                return 0
            a = explore(node.left)
            b = explore(node.right)
            res+= a
            if not node.left and not node.right:
                return node.val
            else:
                return 0


        
        explore(root)
        
        return res