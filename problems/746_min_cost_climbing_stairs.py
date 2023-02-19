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

