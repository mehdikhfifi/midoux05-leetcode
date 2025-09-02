# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        
        def find_height(node):
            if not node:
                return 0
            left = find_height(node.left)
            right = find_height(node.right)
            return 1 + max(left, right)
        
        height = find_height(root) -1

        m = height +1 
        n = pow(2,height +1 ) - 1
        print("m is ",m)
        print("n is ",n)
        matrix = [[""] * n for _ in range(m)]
        matrix[0][(n-1)//2] = str(root.val)
        def explore(node, r, c):
            if not node:
                return 
            matrix[r][c] = str(node.val)
            x = r + 1
            y_l = c - pow(2,height -r -1)
            y_r = c + pow(2,height -r -1)
            explore(node.left, x,y_l)
            explore(node.right, x,y_r)

        explore(root.left, 0 +1 , (n-1)//2 - pow(2, height-1))
        explore(root.right, 0 + 1, (n-1)//2 + pow(2, height-1))

        return matrix
