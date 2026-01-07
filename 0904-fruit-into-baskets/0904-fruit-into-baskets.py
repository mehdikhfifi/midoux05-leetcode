class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        res = 0
        last_dict = {}
        for right, fruit in enumerate(fruits):
            last_dict[fruit] = right    
            if len(last_dict.keys()) > 2:
                key,value = min(last_dict.items(), key = lambda x: x[1])
                del last_dict[key]
                left = value+1
            res = max(res, right - left + 1)
        return res
                