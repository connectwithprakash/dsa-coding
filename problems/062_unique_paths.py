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
        dp = [[0]*n for i in range(m)]
        
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1] 

