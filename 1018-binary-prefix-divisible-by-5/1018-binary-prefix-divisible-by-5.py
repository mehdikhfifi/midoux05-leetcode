class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        
        res = []
        tmp = 0
        tmp_ans = 0 
        for i in range(len(nums)):
            tmp_ans *=2
            if nums[i] == 1:
                tmp_ans += 1
            res.append(tmp_ans % 5 == 0)
            tmp +=1
        return res[::]
