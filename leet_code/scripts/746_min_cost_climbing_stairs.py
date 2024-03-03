"""
# Attempt 1: Recursive solution

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def helper(n):
            if n < 2:
                return 0
            else:
                return min(cost[n-1]+helper(n-1), cost[n-2]+helper(n-2))
        return helper(len(cost))
"""

"""
# Attempt 2: Solution with memoization

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = {}
        def helper(n):
            if n < 2:
                return 0
            if (n-1) not in dp:
                dp[n-1] = helper(n-1)
            if (n-2) not in dp:
                dp[n-2] = helper(n-2)

            return min(cost[n-1]+dp[n-1], cost[n-2]+dp[n-2])
        return helper(len(cost))
"""

# Attempt 3: O(1) space complexity solution

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(2, len(cost)+1):
            previous_cost = min(cost[i-1], cost[i-2])
            if i < len(cost):
                cost[i] = cost[i] + previous_cost
        
        return previous_cost

