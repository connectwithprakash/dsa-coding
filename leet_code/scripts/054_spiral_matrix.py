# Attempt 1: Naive O(n^2) solution
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        spiral_path = {
            "right": "down",
            "down": "left",
            "left": "up",
            "up": "right"
        }

        direction = "right"

        count = 0
        m, n = len(matrix), len(matrix[0])
        total_elems = m*n
        idx, jdx = 0, 0
        result = []
        while count < total_elems:
            if isinstance(matrix[idx][jdx], int):
                result.append(matrix[idx][jdx])
                matrix[idx][jdx] = direction
                count += 1
            else:
                direction = spiral_path[matrix[idx][jdx]]

            if direction == "right":
                jdx += 1
            elif direction == "down":
                idx += 1
            elif direction == "left":
                jdx -= 1
            elif direction == "up":
                idx -= 1
            
            if idx == -1 or idx == m or jdx == -1 or jdx == n:
                idx = max(0, min(idx, m-1))
                jdx = max(0, min(jdx, n-1))
                direction = spiral_path[direction]

        return result

