class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prev_stock = prices[0]
        total_stock = 0
        for i in range(1, len(prices)):
            if prices[i] > prev_stock:
                total_stock += prices[i] - prev_stock
            prev_stock = prices[i]

        return total_stock

