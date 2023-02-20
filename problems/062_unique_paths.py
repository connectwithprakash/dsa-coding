"""
# Recursive solution

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def dfs(x, y):
            if (x == (m-1)) and (y == (n-1)):
                return 1
            else:
                right, left = 0, 0
                if (x < m):
                    right = dfs(x+1, y)
                if (y < n):
                    left = dfs(x, y+1)
                return (right + left)

        return dfs(0, 0)
"""

# DP - memoization solution
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for j in range(n+1)] for i in range(m+1)]
        dp[0][1] = 1
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m][n] 

