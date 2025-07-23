class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        

        n = len(questions)
        dp = [0] * n

        dp[-1] = questions[-1][0]

        i = n-2
        while i >= 0:

            if (i + questions[i][1]+1) < n:
                dp[i] = max(dp[i+1], dp[i+questions[i][1] +1] + questions[i][0])
            else:
                dp[i] = max(questions[i][0], dp[i+1])
                
            i-=1
            # print(dp)
        
        return max(dp)