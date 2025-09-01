# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        

        order = []
        def in_order(node):
            if node is None:
                return
            
            if node.left:
                in_order(node.left)
            order.append(node.val)
            if node.right:
                in_order(node.right)
        in_order(root)
        return min(order[i+1] - order[i] for i in range(len(order)-1) )

