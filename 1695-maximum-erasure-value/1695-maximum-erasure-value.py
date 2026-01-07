class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        prefix = nums[:]
        for index in range(1,len(prefix)):
            prefix[index] = prefix[index-1] + prefix[index]
        left = 0
        last = {}
        res = 0
        for right, num in enumerate(nums):
            if num in last:
                left = max(last[num] + 1, left)
            last[num] = right
            res = max(res, prefix[right] - prefix[left] + nums[left])
        return res
