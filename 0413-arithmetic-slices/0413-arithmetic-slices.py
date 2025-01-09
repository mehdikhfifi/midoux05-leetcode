class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        

        if len(nums) < 3:
            return 0
        n = len(nums)
        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = 0


        # recurrence relation
        total_slices = 0

        for i in range(2,n):

            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                dp[i] = dp[i-1] + 1
            else:
                dp[i] = 0
                # no new additional arithmetic slices have been added as a result of the new element

                
            
            total_slices += dp[i]
        
        return total_slices