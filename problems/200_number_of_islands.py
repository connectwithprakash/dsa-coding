class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        i, j = 0, 0
        m, n = len(grid), len(grid[0])
        count = 0
        grid_coords = [(x, y) for x in range(m) for y in range(n)]
        def traverse_island(x, y):
            grid_coords.remove((x,y))
            if grid[x][y] == "1":
                for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    x_new, y_new = x+dx, y+dy
                    if (0 <= x_new < m) and (0 <= y_new < n) and (grid[x_new][y_new] == "1"):
                        if (x_new, y_new) in grid_coords:
                            traverse_island(x_new, y_new)
                return 1
            else:
                return 0
            
        while len(grid_coords):
            sr, sc = grid_coords[0]
            if (sr,sc) in grid_coords:
                count+= traverse_island(sr, sc)            
            
        return count

