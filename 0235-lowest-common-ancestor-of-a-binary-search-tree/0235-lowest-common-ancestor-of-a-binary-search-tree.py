# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        

        def explore(node):
            z = node.val
            if (p.val < z) and (q.val < z) and node.left:
                return explore(node.left)
            if (p.val> z) and (q.val> z) and node.right:
                return explore(node.right)
            return node

        return explore(root)