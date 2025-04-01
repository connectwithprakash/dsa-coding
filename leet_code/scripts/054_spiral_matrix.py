class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
#         spiral_path = {
#             "right": "down",
#             "down": "left",
#             "left": "up",
#             "up": "right"
#         }

#         direction = "right"

#         count = 0
#         m, n = len(matrix), len(matrix[0])
#         total_elems = m*n
#         idx, jdx = 0, 0
#         result = []
#         while count < total_elems:
#             if isinstance(matrix[idx][jdx], int):
#                 result.append(matrix[idx][jdx])
#                 matrix[idx][jdx] = direction
#                 count += 1
#             else:
#                 direction = spiral_path[matrix[idx][jdx]]

#             if direction == "right":
#                 jdx += 1
#             elif direction == "down":
#                 idx += 1
#             elif direction == "left":
#                 jdx -= 1
#             elif direction == "up":
#                 idx -= 1
            
#             if idx == -1 or idx == m or jdx == -1 or jdx == n:
#                 idx = max(0, min(idx, m-1))
#                 jdx = max(0, min(jdx, n-1))
#                 direction = spiral_path[direction]

#         return result
        
        # Another solution would be to create a boundary and keep on shrinking
        # as we move inward
        m, n = len(matrix), len(matrix[0])
        left, right, top, bottom = 0, n-1, 0, m-1
        result = []
        while left <= right and top <= bottom:
            # Move right from top
            for y in range(left, right+1):
                result.append(matrix[top][y])
            top += 1
            
            # Move bottom from right
            for x in range(top, bottom+1):
                result.append(matrix[x][right])
            right -= 1
            
            # Check if there is no bottom to traverse
            if top <= bottom:
                # Move left from bottom
                for y in range(right, left-1, -1):
                    result.append(matrix[bottom][y])
                bottom -= 1
            
            # Chek if there is no left to traverse
            if left <= right:
                # Move up from left
                for x in range(bottom, top-1, -1):
                    result.append(matrix[x][left])
                left += 1
                
        return result

