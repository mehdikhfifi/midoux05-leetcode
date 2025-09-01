# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        

        prev = None
        res = float('inf')


        def in_order(node):
            nonlocal res, prev
            if not node:
                return 
            in_order(node.left)
            if prev != None:
                res = min(res, node.val - prev)
            prev = node.val
            in_order(node.right)

        in_order(root)
        return res

