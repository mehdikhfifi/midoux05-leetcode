class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        

        mydict = {}
        left = 0
        res = 0 

        for right, letter in enumerate(s):
            if letter in mydict:
                mydict[letter] +=1
            else:
                mydict[letter] = 1
            mx = max(mydict.values())
            while (right - left + 1 - mx) > k: 
                mydict[s[left]] -=1
                left+=1
            res = max(res, right - left + 1)
        return res
