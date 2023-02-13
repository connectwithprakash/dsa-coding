class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        indices = [(sr, sc)]
        indices_visited = []
        m, n = len(image)-1, len(image[0])-1
        starting_pixel_color = image[sr][sc]
        for x, y in indices:
            image[x][y] = color
            indices_visited.append((x,y))
            for dx, dy in [(-1, 0), (0, -1), (1, 0), (0,1)]:
                x_new = x+dx
                y_new = y+dy
                if (0 <= x_new <= m) & (0 <= y_new <= n):
                    if ((x_new, y_new) not in indices_visited) and (image[x_new][y_new] == starting_pixel_color):
                        indices.append((x_new, y_new))

        return image

