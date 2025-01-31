class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        

        # colorful when there are no adjacently similar balloon
        n = len(neededTime)

        dp = n*[0]
        dp[0] = 0
        

        for i in range(1,n):

            if colors[i-1] != colors[i]:
                dp[i] = dp[i-1] 
            else:

                dp[i] = dp[i-1] + min(neededTime[i-1], neededTime[i])
                neededTime[i] = max(neededTime[i], neededTime[i - 1])
            
        return dp[-1]

            
            
