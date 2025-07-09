from collections import defaultdict
from collections import deque

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # strongly coonnected components right, you're just trying to find all the sink nodes in the 
        n = len(graph)
        adjacency_list = {i : graph[i] for i in range(len(graph))}

        reverse_adjacency_list = {i : [] for i in range(len(graph))}

        for i in range(n):
            for neighbor in adjacency_list[i]:
                reverse_adjacency_list[neighbor].append(i)
        # start at the terminal nodes
        q = deque()
        safe = set()
        outdegrees = [len(adjacency_list[i]) for i in range(n)]

        for i in range(n):
            if outdegrees[i] == 0:
                q.append(i)

        while q:
            node = q.popleft()
            safe.add(node)
            # go to its parents
            for parent in reverse_adjacency_list[node]:
                outdegrees[parent] -=1
                if outdegrees[parent] ==0:
                    q.append(parent)

        

        return list(sorted(safe))







        


        


        