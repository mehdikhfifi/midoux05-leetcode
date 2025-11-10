class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        stack  = []
        for n in nums:

            while stack and stack[-1] > n:
                stack.pop()

            if n > 0  and (not stack or stack[-1] < n):
                res +=1
                stack.append(n)
        return res


    #     counter = 0
    #     def longest_non_zero_span(x):
    #         best = (0,-1)
    #         start = 0
    #         i = 0
    #         n = len(x)
    #         while i < n:
    #             if x[i] == 0:
    #                 i +=1
    #                 continue
    #             start = i
    #             min_val = x[start]
    #             while i < n and x[i] !=0:
    #                 min_val = min(min_val, x[i])
    #                 i +=1
    #             end = i-1
    #             return (start, end), min_val
    #     def run_operation(best, min_val):
    #         nonlocal nums
    #         for i in range(best[0], best[1]+1):
    #             if nums[i] == min_val:
    #                 nums[i] =0
    #     while sum(nums) !=0:
    #         best,min_val = longest_non_zero_span(nums)
    #         run_operation(best, min_val)
    #         counter +=1
    #     return counter





        