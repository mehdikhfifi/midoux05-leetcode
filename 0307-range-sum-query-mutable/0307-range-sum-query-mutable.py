class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.tree = [0] * (2 * self.n)
        self.build(nums)
    
    def build(self, nums: List[int]):
        # leaves 
        for i in range(self.n):
            self.tree[i+self.n] = nums[i]
        # parents
        for i in range(self.n-1, 0, -1):
            self.tree[i] = self.tree[2*i] + self.tree[2*i+1]
        
    def update(self, index: int, val: int) -> None:
        index += self.n
        self.tree[index] = val
        # update parents
        parent = index
        while parent > 1:
            parent //=2
            self.tree[parent] = self.tree[parent*2] + self.tree[parent*2 + 1]
        

    def sumRange(self, left: int, right: int) -> int:
        left += self.n
        right += self.n +1
        res =0
        while left < right:
            if left %2 == 1:
                res += self.tree[left]
                left +=1
            if right % 2 == 1:
                right -=1
                res += self.tree[right]
            left //=2
            right //=2
        
        return res

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)