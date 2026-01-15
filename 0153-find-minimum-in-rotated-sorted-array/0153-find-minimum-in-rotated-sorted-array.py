class Solution:
    def findMin(self, nums: List[int]) -> int:

        left = 0
        right = len(nums) - 1
        ans = float('inf')
        while left <= right:
            mid = (left + right) // 2 
            print(left, mid, right)
            ans = min(ans, nums[mid], nums[left], nums[right])
            if nums[mid] > nums[left]:
                left = mid + 1
            else:
                right = mid - 1
        return ans 

                


            

            