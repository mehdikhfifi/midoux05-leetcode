class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        
        new_banned = set()
        for x in banned:
            if x <= n:
                new_banned.add(x)

        total = 0

        i = 0 
        num_numbers = 0


        for i in range(1, n+1):

            if i in new_banned:
                continue
            if i + total > maxSum:
                break
            total +=i
            num_numbers +=1
        return num_numbers