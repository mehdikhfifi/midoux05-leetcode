class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        
        dp = [0, -inf, -inf]
        for i in nums:
            tdp = dp[:]
            for j in range(3):
                print(j)
                print((j + i) % 3)
                tdp[j] = max(dp[j], dp[(j + i) % 3] + i)
            dp = tdp
        return dp[0]