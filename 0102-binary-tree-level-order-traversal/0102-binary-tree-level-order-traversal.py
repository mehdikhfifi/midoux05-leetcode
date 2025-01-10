from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        result = []


        if not root:
            return result

        
        queue = deque([root])

        while queue:
            level_size = len(queue)
            cur_level = []
            
            for _ in range(level_size):
                current_node = queue.popleft()
                cur_level.append(current_node.val)


                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)

            result.append(cur_level)
            
        return result

