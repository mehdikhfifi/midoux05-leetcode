class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        
        if k % 2 == 0 or k % 5 == 0:
            return -1
        else:
            temp = 1
            res = 1
            while temp % k != 0:
                temp *= 10
                temp +=1
                res +=1
            return res


              