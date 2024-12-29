class Solution:
    def numSquares(self, n: int) -> int:
        

        least = n

        dp = list(range(n+1))

        for i in range(1,n+1):

            for j in range(i):

                if i - j**2 >= 0:
                    dp[i] = min(dp[i], dp[i-j*j] + 1)
                else:
                    break

        return dp[-1]
        

        

        
