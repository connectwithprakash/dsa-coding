class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def traverse_island(x, y, has_boundary):
            if (x == 0) or (x == (m-1)) or (y == 0) or (y == (n-1)):
                has_boundary = True
            grid[x][y] = 2 * (not has_boundary) 
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                x_new, y_new = x+dx, y+dy
                if (0 <= x_new < m) and (0 <= y_new < n) and (grid[x_new][y_new] == 1):
                    traverse_island(x_new, y_new, has_boundary)

        count = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    traverse_island(i, j, False)
                if grid[i][j] == 2:
                    count += 1
        return count

