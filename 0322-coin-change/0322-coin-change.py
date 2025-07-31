class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        

        n = len(coins)
        dp = [float('inf')] * (amount +1)
        dp[0] = 0


        for i in range(len(coins)):
            for w in range((amount)+1):

                if coins[i] <= w:
                    dp[w] = min(dp[w], dp[w-coins[i]] + 1)
        
        return dp[-1] if dp[-1] != float('inf') else -1