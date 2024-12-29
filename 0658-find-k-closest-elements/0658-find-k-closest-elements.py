import heapq


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        

        max_heap = []



        for num in arr:

            heapq.heappush(max_heap, (-abs(num-x), -num))

            if len(max_heap) > k:
                heapq.heappop(max_heap)


            
        result = [-pair[1] for pair in max_heap]

        return sorted(result)