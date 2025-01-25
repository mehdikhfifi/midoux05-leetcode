class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        



# 3,1,5,8
# the subrpoblems are derived by first looking at which number is last popped

        nums = [1] + nums + [1]

        dp = {}
        
        # this dp hashmap is for memoization


        def dfs(l, r):
            # this function finds the maximum coins you can collect between range l and r

            # first handle the base cases
            if l > r:
                return 0 # shit don't make sense
            if (l,r) in dp:
                return dp[(l,r)]

            # otherwise brute force and find the optimal number of coins recursively
            dp[(l,r)] = 0
            for i in range(l, r+1):
                # finds which index in l to r should be removed last, 
                # the one that leads to the most optimal maximum number of coins
                coins = nums[i] * nums[r+1] * nums[l-1] # if i is popped last, this is the last operation
                coins += dfs(l, i-1) + dfs(i+1, r)
                dp[(l,r)] = max(coins, dp[(l,r)])
            return dp[(l,r)]
        return dfs(1,len(nums) -2)

