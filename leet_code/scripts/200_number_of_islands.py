class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        count = 0
        def traverse_island(x, y):
            grid[x][y] = 'i'
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                x_new, y_new = x+dx, y+dy
                if (0 <= x_new < m) and (0 <= y_new < n) and (grid[x_new][y_new] == '1'):
                    traverse_island(x_new, y_new)
            
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    traverse_island(i, j)
                    count += 1

        return count

