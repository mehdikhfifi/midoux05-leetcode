
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:

        # first formulate count array

        cnt = [0] * (max(nums)+1)


        for x in nums:
            cnt[x] +=1

        print(cnt)

        dp = [0 for _ in range(len(cnt))]

        dp[0] = 0
        dp[1] = cnt[1]

        for i in range(2,len(dp)):

            dp[i] = max(dp[i-1], cnt[i] * i + dp[i-2])
        
        return dp[-1]
        