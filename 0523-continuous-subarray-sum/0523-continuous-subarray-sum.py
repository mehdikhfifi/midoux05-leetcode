class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        


        hashmap = {0:-1}
        total = 0

        
        for i in range(len(nums)):
            total += nums[i]
            remainder = total % k

            if remainder not in hashmap:
                hashmap[remainder] = i
            elif i - hashmap[remainder]  > 1:
                return True
        
        return False


# solution makes hell sense