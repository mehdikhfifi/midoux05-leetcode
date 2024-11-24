import heapq

from collections import defaultdict
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        

        graph = defaultdict(list)

        for u, v, w in flights:
            graph[u].append((v,w))


        heap = [(0,src,0)]

        visited = {}



        while heap:

            cost, u, stops = heapq.heappop(heap)

            if u == dst:
                return cost

            if stops > k:
                continue
            
            if u in visited and visited[u] < stops:
                continue

            

            visited[u] = stops

            for v, w in graph[u]:
                heapq.heappush(heap, (cost+w, v, stops +1))

        
        return -1