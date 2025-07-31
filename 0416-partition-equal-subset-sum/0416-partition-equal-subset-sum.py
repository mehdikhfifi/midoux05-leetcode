class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        target = total // 2

        dp = [False] * (target + 1)
        dp[0] = True

        for i in range(len(nums)):
            for w in range(target, nums[i]-1, -1):
                if nums[i] <= w:
                    dp[w] = dp[w] or dp[w-nums[i]]
        return dp[-1]