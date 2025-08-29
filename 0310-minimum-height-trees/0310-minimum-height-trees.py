from collections import defaultdict
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return [i for i in range(n)]
        graph = defaultdict(list)

        degree = [0] * n
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
            degree[x] +=1
            degree[y] +=1
        for node in graph.keys():
            degree[node] = len(graph[node])
        leaves = deque([i for i in range(n) if degree[i] == 1])

        remaining_nodes = n

        while remaining_nodes >2:
            size = len(leaves)
            remaining_nodes -= size
            for _ in range(size):
                leaf = leaves.popleft()
                degree[leaf] = 0
                for parent in graph[leaf]:
                    degree[parent] -=1
                    if degree[parent] ==1:
                        leaves.append(parent)
        return list(leaves)

            

        
        


        