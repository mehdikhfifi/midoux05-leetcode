class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        dp = [0] * n

        for i in range(n-1, -1, -1):
            cost1 = costs[0] + (dp[i+1] if i + 1 < n else 0)

            j = i

            while j < n and days[j] <= days[i] + 6:
                j +=1
            cost7 = costs[1] + (dp[j] if j < n else 0)

            k = i

            while k < n and days[k] <= days[i] + 29:
                k+=1
            
            cost30 = costs[2] + (dp[k] if k < n else 0)


            dp[i] = min(cost1, cost7, cost30)

        
        return dp[0]








