# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        

        if not root:
            return []
        
        def explore(node, level, res):
            if not node:
                return 
            if len(res)<= level:
                res.append([])
            
            res[level].append(node.val)

            explore(node.left, level+1, res)
            explore(node.right, level+1, res)
            return res

        return explore(root, 0, [])