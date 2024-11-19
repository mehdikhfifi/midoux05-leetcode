from typing import List

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        if len(nums) < k:
            return 0

        # Sliding window setup
        current_sum = sum(nums[:k])
        element_count = {}
        for i in range(k):
            element_count[nums[i]] = element_count.get(nums[i], 0) + 1

        maximum = 0
        # Check if the first window is valid
        if len(element_count) == k:
            maximum = max(maximum, current_sum)

        # Sliding window logic
        for i in range(k, len(nums)):
            # Add the new element
            current_sum += nums[i]
            element_count[nums[i]] = element_count.get(nums[i], 0) + 1

            # Remove the old element
            current_sum -= nums[i - k]
            element_count[nums[i - k]] -= 1
            if element_count[nums[i - k]] == 0:
                del element_count[nums[i - k]]

            # Check if the current window is valid
            if len(element_count) == k:
                maximum = max(maximum, current_sum)

        return maximum
