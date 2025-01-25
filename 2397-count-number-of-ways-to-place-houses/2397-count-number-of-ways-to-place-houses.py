class Solution:
    def countHousePlacements(self, n: int) -> int:
        MOD = 10**9 + 7

        # Base cases
        if n == 1:
            return 4

        # DP array for one side of the street
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 2

        # Fill the DP table
        for i in range(2, n + 1):
            dp[i] = (dp[i - 1] + dp[i - 2]) % MOD

        # Total ways for both sides
        result = (dp[n] * dp[n]) % MOD
        return result