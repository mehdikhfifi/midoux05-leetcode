from collections import defaultdict
class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        


        graph = defaultdict(list)
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        res = 0
        def dfs(node, parent):
            total = values[node]

            for child in graph[node]:
                if child != parent:
                    total += dfs(child, node)
            
            if total % k == 0:
                nonlocal res 
                res +=1
            return total
        dfs(0,-1)

        return res



        

        
        




