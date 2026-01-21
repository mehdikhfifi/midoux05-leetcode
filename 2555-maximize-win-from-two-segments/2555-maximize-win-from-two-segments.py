class Solution:
    def maximizeWin(self, pos: List[int], k: int) -> int:
        
        n = len(pos)
        res = 0
        seg1 = 0
        prev = 0
        next_ = 0

        for i in range(n):
            while (next_ < n) and (pos[next_] - pos[i] <= k):
                next_+=1
            while (prev < n) and (pos[i] - pos[prev]) > k:
                prev+=1
            res = max(res,seg1 + next_ - i )
            seg1 = max(seg1, i - prev + 1)
        return res
