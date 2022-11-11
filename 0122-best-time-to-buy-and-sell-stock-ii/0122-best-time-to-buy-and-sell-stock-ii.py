class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for r in range(len(prices) - 1):
            if prices[r + 1] > prices[r]:
                profit += prices[r + 1] - prices[r]
        return profit