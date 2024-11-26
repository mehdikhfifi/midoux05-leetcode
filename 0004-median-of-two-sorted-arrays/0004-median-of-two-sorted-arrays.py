class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        x = nums1 + nums2
        x = list(sorted(x))
        
        if len(x) % 2 != 0:
            return x[len(x)//2]
        else:
            return (x[(len(x)//2) -1] + x[(len(x)//2)])/2