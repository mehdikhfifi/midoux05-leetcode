class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        if sum(nums) % 2 != 0:
            return False

        n = len(nums)
        capacity = sum(nums) // 2

        dp = [[True] * (capacity+1) for _ in range(n +1)]

        dp[0][0] = 0
        for j in range(capacity+1):
            dp[0][j] = False
        
        for i in range(n+1):
            dp[i][0] = True
        
        for i in range(1,n+1):
            for j in range(1, capacity+1):

                dp[i][j] = dp[i-1][j] # you do not pick a number

                if j >= nums[i-1]: 
                    dp[i][j] =  dp[i-1][j] or dp[i-1][j - nums[i-1]]
        
        return dp[-1][-1]



        





        
