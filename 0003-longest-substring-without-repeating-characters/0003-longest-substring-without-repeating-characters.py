class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        last = {}
        left = 0
        ans = 0
        for right, letter in enumerate(s):
            if letter in last:
                left = max(last[letter] + 1, left)
            last[letter] = right
            ans = max(ans, right - left + 1)
            print(left, right, ans)
        return ans
