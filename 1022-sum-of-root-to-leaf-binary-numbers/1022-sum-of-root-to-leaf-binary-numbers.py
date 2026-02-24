# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(node, sofar):
            nonlocal res
            if not node:
                return
            if not node.left and not node.right:
                # print(sofar)
                res += int(sofar + str(node.val), 2)
            else:
                print(node.val)
                dfs(node.left, sofar + str(node.val)) 
                dfs(node.right, sofar + str(node.val))

                
        
        dfs(root, '')
        return res
            