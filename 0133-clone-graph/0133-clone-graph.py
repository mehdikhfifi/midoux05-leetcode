"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, root: Optional['Node']) -> Optional['Node']:
        if not root:
            return None
        hashmap = {}
        def explore(node):
            if node.val in hashmap.keys():
                return hashmap[node.val]

            new_node = Node(node.val)
            hashmap[node.val] = new_node 
            for child in node.neighbors:
                new_node.neighbors.append(explore(child))           
            return new_node
        
        return explore(root)
        


        



