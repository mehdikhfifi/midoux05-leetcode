class Solution:
    def rob(self, nums: List[int]) -> int:

        

        if not nums:
            return 0
        n = len(nums)
        if n == 1 or n == 2:
            return max(nums)
        

        def rob_linear(nums, start, end):
            dp = [0] * (end - start +1)

            dp[0] = nums[start]
            dp[1] = max(nums[start], nums[start + 1])
            for i in range(2, end-start + 1):
                dp[i] = max(dp[i-1], dp[i-2] + nums[start +i])
            
            return dp[-1]
        
        rob1 = rob_linear(nums, 0, n-2)
        rob2 = rob_linear(nums, 1, n-1)

        return max(rob1, rob2)        

