class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0 for _ in range(n)] for _ in range(n)]

        for right in range(2, n):
            for left in range(right - 2, -1, -1):
                dp[left][right] = max([dp[left][m] + dp[m][right] + nums[left] * nums[m] * nums[right] for m in range(left + 1, right)])
        
        return dp[0][n - 1]