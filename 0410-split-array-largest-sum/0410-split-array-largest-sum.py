class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)

        def condition(mid):
            num_subarrays = 0
            temp = 0
            for x in nums:
                if temp + x > mid:
                    num_subarrays +=1
                    temp = x
                else:
                    temp += x
            return num_subarrays
        while left <= right:
            mid = (left + right  ) // 2 
            print(mid, condition(mid))
            if condition(mid) >= k:
                left = mid +1
            else:
                right = mid -1
        return left

            