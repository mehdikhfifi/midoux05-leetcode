class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        MOD_VAL = 10**9 + 7

        n = len(grid[0])
        dp = [[[0 for _ in range(k)] for _ in range(n)] for _ in range(m)]

        dp[0][0][grid[0][0]%k] = 1 
        
        for i in range(1,m):
            val = grid[i][0]
            for mod in range(k):
                dp[i][0][(val + mod)%k] = dp[i-1][0][mod]  
            
        for j in range(1,n):
            val = grid[0][j]
            for mod in range(k):
                dp[0][j][(val + mod)%k] = (dp[0][j-1][mod]) 

        for i in range(1, m):
            for j in range(1, n):
                val = grid[i][j]
                for mod in range(k):
                    dp[i][j][(val + mod) % k] = dp[i][j - 1][mod] + dp[i - 1][j][mod]
        print(MOD_VAL) 
        return dp[-1][-1][0] % MOD_VAL
