class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        answer = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    if i not in answer and j not in answer:
                        answer.append(i)
                        answer.append(j)
        
        return answer


        