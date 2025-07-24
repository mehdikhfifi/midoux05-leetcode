class Solution:
    def numDecodings(self, s: str) -> int:
        



        n = len(s)
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 0 if s[0] == '0' else 1

        for i in range(1,n):
            
            char = s[i]
            prev_1 = s[i-1]
            
            if char == '0':
                if int(prev_1 + char) in range(10,27):
                    dp[i+1] = dp[i+1-2]
                else:
                    dp[i+1] =0
            else:
                if int(prev_1 + char) in range(10,27):
                    dp[i+1] = dp[i+1-2] + dp[i+1-1]
                else:
                    dp[i+1] = dp[i+1-1]
            print(dp)
        return dp[-1]



            # modifying dp[i+1]            