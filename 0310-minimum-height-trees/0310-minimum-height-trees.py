from collections import defaultdict

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <=2:
            return list(range(n))

        graph = {i : [] for i in range(n)}

        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
        

        
        leaves = [i for i in graph if len(graph[i]) == 1]

        remaining = n

        while remaining > 2:

            remaining -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)

                if len(graph[neighbor]) ==1:
                    new_leaves.append(neighbor)
            leaves= new_leaves
            
        
        return leaves


        

