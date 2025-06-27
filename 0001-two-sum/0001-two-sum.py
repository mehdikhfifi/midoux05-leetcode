class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:



        hastable = {}

        for index, nums in enumerate(nums):


            
            if target - nums in hastable:
                return list(sorted([hastable[target-nums], index]))
            else:
                hastable[nums] = index
        

