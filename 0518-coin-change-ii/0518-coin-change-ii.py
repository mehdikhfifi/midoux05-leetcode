class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        n = len(coins)
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in range(n):
            for w in range(amount + 1):
                if coins[i] <= w:
                    dp[w] += dp[w - coins[i]] 
        print(dp)
        return dp[amount]