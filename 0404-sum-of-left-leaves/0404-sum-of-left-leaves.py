# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        def explore(node, isLeft):
            if not node:
                return 0
            if not node.left and not node.right:
                return node.val if not isLeft else 0 
            return explore(node.left, False) + explore(node.right, True)
        
        return explore(root.left, False) + explore(root.right, True)