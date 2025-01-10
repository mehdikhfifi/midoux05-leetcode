# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(node):


            if not node:
                return 0, True
            
            left_height, isbalancedleft = helper(node.left)
            right_height, isbalancedright = helper(node.right)

            is_balanced = isbalancedleft and isbalancedright and abs(left_height - right_height) <= 1


            return max(left_height, right_height) + 1, is_balanced 








        

        return helper(root)[1]
        