class Solution:
    def optimalDivision(self, nums: List[int]) -> str:

        if len(nums) == 1: 
            return str(nums[0])
        if len(nums) == 2:
            return str(nums[0]) + "/" + str(nums[1]) 


        my_string = str(nums[0]) + "/(" + str(nums[1])

        for x in nums[2:]:
            
            my_string += "/" + str(x)

        my_string += ")"

        return my_string