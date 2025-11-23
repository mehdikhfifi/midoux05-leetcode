class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        

        dp = [[0 for _ in range(3)] for _ in range(len(nums))] 


        dp[-1][nums[-1]%3] = nums[-1]

        for i in range(len(nums)-2, -1,-1):

            
            x1 = dp[i+1][0] + nums[i]
            x2 = dp[i+1][1] + nums[i]
            x3 = dp[i+1][2] + nums[i]
            x4 = nums[i]
            dp[i][x1%3] = max(dp[i][x1%3], x1)
            dp[i][x2%3] = max(dp[i][x2%3], x2)
            dp[i][x3%3] = max(dp[i][x3%3], x3)
            dp[i][x4%3] = max(dp[i][x4%3], x4)
            dp[i][0] = max(dp[i][0], dp[i+1][0])
            dp[i][1] = max(dp[i][1], dp[i+1][1])
            dp[i][2] = max(dp[i][2], dp[i+1][2])
        return dp[0][0]
