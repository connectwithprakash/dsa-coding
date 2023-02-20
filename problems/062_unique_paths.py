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

