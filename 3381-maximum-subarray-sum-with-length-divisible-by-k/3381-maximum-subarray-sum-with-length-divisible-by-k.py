class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        nums.insert(0,0)
        for index,value in enumerate(nums):
            if index == 0:
                continue
            nums[index] = nums[index] + nums[index-1]
        
        n = len(nums)
        
        res = -float('inf')


        for i in range(k):
            tmp_arr = []
            for j in range(i,n-k,k):
                tmp_arr.append(nums[j+k] - nums[j])
            # print(tmp_arr)

            # run kadane's algo
            running_sum = 0
            for x in tmp_arr:
                running_sum += x
                # print(running_sum)
                res = max(running_sum, res)
                if running_sum < 0:
                    running_sum = 0
        return res





            
