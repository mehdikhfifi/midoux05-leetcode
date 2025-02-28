from collections import defaultdict

class Solution:
    def longestPalindrome(self, s: str) -> int:
        

        hashmap = defaultdict(lambda: 0)
        
        for x in s: 
            hashmap[x] +=1
        

        res = 0
        # print(hashmap.keys())
        # print(hashmap.values())
        odd = False
        for m in hashmap.values():
            if m % 2 == 0:
                res+=m
            else:
                res += max(0,m-1)
                odd = True
               
        
        return res + (1 if odd == True else 0)