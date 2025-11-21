class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        

        fl = [[-1,-1] for _ in range(26)] 

        for index, char in enumerate(s):
            alpha = ord(char) - ord('a')
            # print(alpha)
            if fl[alpha][0] == -1:
                fl[alpha][0] = index
                fl[alpha][1] = index
            elif fl[alpha][1] != -1:
                fl[alpha][1] = index
        # print(fl)
        res = 0
        for alphabet in range(26):
            if (fl[alphabet] == [-1,-1]) or (fl[alphabet][0] == fl[alphabet][1]):
                continue
            print(fl[alphabet])
            temp_set = set()
            for i in range(fl[alphabet][0]+1, fl[alphabet][1]):
                temp_set.add(s[i])
            res += len(temp_set)
        
        return res



            