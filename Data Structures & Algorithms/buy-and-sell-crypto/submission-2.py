class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        i, j = 0, 1
        profit = prices[j] - prices[i]
        """
        max_profit = 0

        i, j = 0, 1
        while j < len(prices):
            profit = prices[j] - prices[i]
            print(i, j, profit)
            if profit < 0:
                i = j
                j = i + 1
            else:
                j += 1
            max_profit = max(profit, max_profit)

        return max_profit