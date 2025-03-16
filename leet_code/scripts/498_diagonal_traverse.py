"""
Input: Matrix of numbers
Output: Array with numbers ordering in diagonal traversal manner
Idea: An iead would be to get a list of dynamic list where we store 
all the diagonal element from first 0 to n_rows and then from n_rows+1 
to n_cols, basically to move across the L shape and store the diagonal 
of each of them. Then as a second step, flip the elements of the array 
of the array at 1 skip.T: O(n*k), S: O(n*k)

Another idea would be to traverse the matrix in a zigzag pattern, alternating 
between moving up-right and down-left. Keep track of the current direction and 
handle boundary cases to change direction when hitting the edges of the matrix.
T: O(m*n), S: O(1) where m and n are the dimensions of the matrix.
"""


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # results = []
        # m, n = len(mat), len(mat[0])
        # # Top to bottom
        # for kdx in range(m):
        #     idx = kdx
        #     jdx = 0
        #     diag_elements = []
        #     while idx >= 0 and  jdx < n:
        #         diag_elements.append(mat[idx][jdx])
        #         idx -= 1
        #         jdx += 1
        #     results.append(diag_elements)
        # # left to right
        # for kdx in range(1, n):
        #     idx = m-1
        #     jdx = kdx
        #     diag_elements = []
        #     while jdx < n and idx >= 0:
        #         diag_elements.append(mat[idx][jdx])
        #         idx -= 1
        #         jdx += 1
        #     results.append(diag_elements)
        # # Correct the ordering
        # n_diags = len(results)
        # result = []
        # for idx in range(n_diags):
        #     if idx % 2: # flip the numbers
        #         for jdx in range(len(results[idx])):
        #             result.append(results[idx].pop())
        #     else: # don't flip
        #         result.extend(results[idx])

        # Another approach
        result = []
        up = True  # Flag to determine the current direction (up-right or down-left)
        m, n = len(mat), len(mat[0])
        idx, jdx = 0, 0  # Starting position

        for _ in range(m*n):  # Iterate through all elements in the matrix
            result.append(mat[idx][jdx])  # Add current element to result

            if up:  # Moving up-right
                dx, dy = idx - 1, jdx + 1  # Calculate next position
                if dx == -1:  # Hit top boundary
                    dx, dy = idx, jdx + 1
                    up = False  # Change direction
                if dy == n:  # Hit right boundary
                    dx, dy = idx + 1, jdx
                    up = False  # Change direction
            else:  # Moving down-left
                dx, dy = idx + 1, jdx - 1  # Calculate next position
                if dy == -1:  # Hit left boundary
                    dx, dy = idx + 1, jdx
                    up = True  # Change direction
                if dx == m:  # Hit bottom boundary
                    dx, dy = idx, jdx + 1
                    up = True  # Change direction

            idx, jdx = dx, dy  # Update current position
        
        return result

