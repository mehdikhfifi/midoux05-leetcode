class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:

        N = len(nums)


        prefix = [0]*(N+1)
        for i in range(N):
            prefix[i+1] = prefix[i] + nums[i]
        def range_sum(l, r):
            return prefix[r+1] - prefix[l]

        decreasing = []
        i = 0
        while i < N:
            
            left = i
            if i + 1 < N and nums[i+1] < nums[i]:
                right = i + 1 
                while right + 1 < N and nums[right+1] < nums[right]:
                    right +=1
                decreasing.append((left,right))
                i = right + 1
            else:
                i+=1
        def debug_calls(name):
            def decorator(fn):
                def wrapper(*args):
                    print(f"{name} called with {args}")
                    return fn(*args)
                return wrapper
            return decorator

        # @debug_calls("shrink_right")
        # @lru_cache(None)
        def shrink_right(x):
            temp = 0
            res = -inf
            while x+1 < N and nums[x+1] > nums[x]:
                temp += nums[x+1]
                res = max(res, temp)
                x+=1
            return res
        
        # @lru_cache(None)
        def shrink_left(x):
            temp = 0
            res = -inf
            while x-1 >= 0 and nums[x-1] < nums[x]:
                temp += nums[x-1]
                res = max(res, temp)
                x-=1
            return res
        res = -inf
        for left_bound, right_bound in decreasing:
            first = shrink_left(left_bound)
            third = shrink_right(right_bound)
            middle =  range_sum(left_bound, right_bound)
            res = max(res, first + third + middle)
        return res

