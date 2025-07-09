class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        
        dp = [1] * len(pairs)

        new_pairs = list(sorted(pairs, key = lambda x: x[1]))

        print(new_pairs)

        # version of LIS

        for i in range(len(pairs)):
            for j in range(i):

                if new_pairs[j][1] < new_pairs[i][0]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    
        return max(dp)