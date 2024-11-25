class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        
        if len(nums) ==1:
            return nums[0]

        
        x = set(nums)


        nums = Counter(nums)


        for i in x:
            if nums[i] ==1:
                return i
