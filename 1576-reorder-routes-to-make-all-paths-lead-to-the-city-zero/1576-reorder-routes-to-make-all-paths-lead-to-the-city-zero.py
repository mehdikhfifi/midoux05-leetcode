from collections import defaultdict
from collections import deque
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
    
        undirected_graph = {i:[] for i in range(n) }
        directed_graph = {i : [] for i in range(n)}

        for x,y in connections:
            undirected_graph[x].append(y)
            undirected_graph[y].append(x)
            directed_graph[x].append(y)
        visited = set()

        res = 0
        q = deque([0])
        visited.add(0)

        while q:
            node = q.pop()
            print(node)

            for neighbor in undirected_graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)
                    if neighbor  in directed_graph[node]:
                        res+=1

        return res





