class Solution:
    def knightDialer(self, n: int) -> int:
        MODULO = pow(10,9) + 7
        
        moves = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4]
        }
        

        dp = [ [0 for _ in range(10)] for _ in range(n+1)]


        for i in range(10):
            dp[1][i] = 1
        

        for i in range(2, n+1):
            for digit in range(10):
                for move in moves[digit]:
                    dp[i][digit] = (dp[i][digit] + dp[i-1][move]) % MODULO  
        

        return sum(dp[n]) % MODULO  