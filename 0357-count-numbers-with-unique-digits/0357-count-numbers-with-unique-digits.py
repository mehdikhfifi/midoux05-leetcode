class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        
        
        if n == 0:
            return 1
        if n ==1 :
            return 10

        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 10

        for i in range(2,n+1):
            tobeadded = 1

            k = i
            
            while k !=1:
                tobeadded *= (10 -(k-1))
                print(tobeadded)
                k-=1
            dp[i] = dp[i-1] + 9*tobeadded
            print(dp)
        return dp[-1]






