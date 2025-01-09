class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        

        if len(nums) < 3:
            return 0
        n = len(nums)



        # recurrence relation
        total_slices = 0
        prev = 0

        for i in range(2,n):

            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                prev = prev + 1
            else:
                prev = 0
                # no new additional arithmetic slices have been added as a result of the new element


            
            total_slices += prev
        
        return total_slices