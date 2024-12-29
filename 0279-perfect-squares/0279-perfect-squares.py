import math
class Solution:
    def numSquares(self, n: int) -> int:
        

        # least = n

        # dp = list(range(n+1))

        # for i in range(1,n+1):

        #     for j in range(i):

        #         if i - j**2 >= 0:
        #             dp[i] = min(dp[i], dp[i-j*j] + 1)
        #         else:
        #             break

        # return dp[-1]
        

        if int(math.sqrt(n))**2 == n:
            return 1

    # Check if n can be written as the sum of two squares
        for i in range(1, int(math.sqrt(n)) + 1):
            if int(math.sqrt(n - i * i))**2 == n - i * i:
                return 2

        # Check if n satisfies 4^k(8m + 7)
        while n % 4 == 0:
            n //= 4
        if n % 8 == 7:
            return 4

        return 3

        
