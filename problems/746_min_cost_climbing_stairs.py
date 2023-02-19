class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def helper(n):
            if n < 2:
                return 0
            else:
                return min(cost[n-1]+helper(n-1), cost[n-2]+helper(n-2))
        return helper(len(cost))

