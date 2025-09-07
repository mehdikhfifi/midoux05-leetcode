import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        
        self.h = [num for num in nums]
        heapq.heapify(self.h)
        self.k = k
        while len(self.h) > self.k:
            heapq.heappop(self.h)

    def add(self, val: int) -> int:
        if len(self.h) < self.k:
            heapq.heappush(self.h, val)
        else:
            if (self.h[0] < val):
                heapq.heappop(self.h)
                heapq.heappush(self.h,val)
        return self.h[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)