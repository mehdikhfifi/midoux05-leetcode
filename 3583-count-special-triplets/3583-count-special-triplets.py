from collections import defaultdict


class Solution:
    def specialTriplets(self, nums: List[int]) -> int:

        MOD = 10**9 + 7
        res = 0
        left = collections.defaultdict(int)
        right = collections.defaultdict(int)
        for x in nums:
            right[x] += 1
        
        for x in nums:
            right[x] -=1

            fleft = left[2*x] % MOD
            fright = right[2*x] % MOD
            res += fleft * fright % MOD
            left[x] +=1 
        return res % MOD