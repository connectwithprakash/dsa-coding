class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = 1e6
        high = 0
        profit = 0
        for price in prices:
            if price < low:
                low = price
                high = 0
            elif price > high:
                high = price
            else:
                pass

            new_profit = (high-low)
            if new_profit > profit:
                profit = new_profit

        return profit
