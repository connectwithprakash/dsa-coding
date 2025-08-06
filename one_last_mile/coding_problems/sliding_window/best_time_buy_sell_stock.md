# Best Time to Buy and Sell Stock

## Problem Statement
You are given an array `prices` where `prices[i]` is the price of a given stock on the `ith` day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

## Examples
```
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
```

## My Approach
I need to find the maximum difference between a future price and a past price. My strategy:
- Track the minimum buy price seen so far
- Calculate profit if we sell at current price
- Update maximum profit if current profit is better

**Key insight**: We can solve this in a single pass by maintaining the minimum price and maximum profit as we go.

## My Solution 1: Two Pointers Approach
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_idx = 0      # Pointer to potential buy day
        sell_idx = 1     # Pointer to potential sell day
        n = len(prices)
        max_profit = 0

        while (sell_idx < n):
            if (prices[sell_idx] > prices[buy_idx]):
                # Profitable transaction possible
                curr_profit = prices[sell_idx] - prices[buy_idx]
                max_profit = max(max_profit, curr_profit)
            else:
                # Found a lower buy price, update buy pointer
                buy_idx = sell_idx
            sell_idx += 1

        return max_profit
```

## My Solution 2: Sliding Window (Cleaner)
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy = prices[0]    # Track minimum price seen so far
        max_profit = 0

        for sell in prices:
            # Calculate profit if we sell at current price
            max_profit = max(max_profit, sell - min_buy)
            # Update minimum buy price if current is lower
            min_buy = min(min_buy, sell)

        return max_profit
```

## Complexity Analysis ✅
- **Time Complexity**: O(n) - Single pass through the array
- **Space Complexity**: O(1) - Only using a few variables

Both solutions are optimal!

## What I Learned
- **This is a sliding window problem** - The "window" is between buy and sell days
- **Greedy approach works** - Always update to the lowest buy price when found
- **Two implementations, same logic** - Solution 1 uses explicit pointers, Solution 2 is more concise
- **Order matters** - Must buy before selling (can't go backwards in time)

## Why Both Solutions Work

### Solution 1 (Two Pointers):
- Explicitly tracks buy and sell indices
- When a lower price is found, moves buy pointer
- Clear visualization of the buy/sell window

### Solution 2 (Min Tracking):
- Tracks minimum price instead of index
- More concise and Pythonic
- Same logic, cleaner implementation

## Key Insight
The maximum profit is the largest difference between a price and the minimum price before it. By tracking the minimum price as we iterate, we can calculate the best profit at each position in O(n) time.