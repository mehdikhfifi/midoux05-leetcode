class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        



        if sum(nums) % k != 0:
            return False

        side_length = sum(nums) // k

        nums.sort(reverse = True)
        def backtrack(index):

            if index == len(nums):
                return all(side == side_length for side in sides)
            
            for i in range(len(sides)):

                if nums[index] + sides[i] <= side_length:

                    sides[i] += nums[index]
                    if backtrack(index+1):
                        return True
                    
                    sides[i] -= nums[index]
                if sides[i] == 0:
                    break
            
            return False


        sides = [0] * k

        return backtrack(0)

