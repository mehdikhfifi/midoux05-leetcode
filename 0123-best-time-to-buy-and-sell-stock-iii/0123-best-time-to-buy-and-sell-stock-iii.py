class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        if not prices:
            return 0

        n = len(prices)
        
        # Step 1: Left-to-Right pass
        left_profit = [0] * n
        min_price = prices[0]
        for i in range(1, n):
            min_price = min(min_price, prices[i])
            left_profit[i] = max(left_profit[i - 1], prices[i] - min_price)
        print(left_profit)
        # Step 2: Right-to-Left pass
        right_profit = [0] * n
        max_price = prices[-1]
        for i in range(n - 2, -1, -1):
            max_price = max(max_price, prices[i])
            right_profit[i] = max(right_profit[i + 1], max_price - prices[i])
        print(right_profit)
        
        # Step 3: Combine results
        max_profit = 0
        for i in range(n):
            max_profit = max(max_profit, left_profit[i] + right_profit[i])
        
        return max_profit


        
