from typing import List

class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        n = len(nums)
        if n == 1:
            return str(nums[0])
        if n == 2:
            return f"{nums[0]}/{nums[1]}"
        
        # Initialize DP tables
        dp = [[0] * n for _ in range(n)]   # Stores max values
        min_dp = [[0] * n for _ in range(n)]  # Stores min values
        exp = [[""] * n for _ in range(n)]   # Stores max expressions
        min_exp = [[""] * n for _ in range(n)]  # Stores min expressions
        
        # Base cases
        for i in range(n):
            dp[i][i] = min_dp[i][i] = nums[i]
            exp[i][i] = min_exp[i][i] = str(nums[i])
        
        # DP computation for subarrays of length > 1
        for length in range(2, n + 1):  # Length of subarray
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = float('-inf')
                min_dp[i][j] = float('inf')
                
                # Try all possible splits
                for k in range(i, j):
                    # Maximize dp[i][j]
                    value = dp[i][k] / min_dp[k+1][j]
                    if value > dp[i][j]:
                        dp[i][j] = value
                        # If k+1 to j contains more than one element, add parentheses
                        if k + 1 == j:
                            exp[i][j] = f"{exp[i][k]}/{min_exp[k+1][j]}"
                        else:
                            exp[i][j] = f"{exp[i][k]}/({min_exp[k+1][j]})"
                    
                    # Minimize min_dp[i][j]
                    value = min_dp[i][k] / dp[k+1][j]
                    if value < min_dp[i][j]:
                        min_dp[i][j] = value
                        # If k+1 to j contains more than one element, add parentheses
                        if k + 1 == j:
                            min_exp[i][j] = f"{min_exp[i][k]}/{exp[k+1][j]}"
                        else:
                            min_exp[i][j] = f"{min_exp[i][k]}/({exp[k+1][j]})"

        return exp[0][n-1]
