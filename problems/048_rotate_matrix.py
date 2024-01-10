# Attempt 1: Transpose and Flip the Matrix Approach
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        # Transpose the matrix
        for idx in range(m):
            for jdx in range(idx, n):
                matrix[idx][jdx], matrix[jdx][idx] = matrix[jdx][idx], matrix[idx][jdx]
            
        # Flip the matrix
        for jdx in range(n//2):
            for idx in range(m):
                matrix[idx][jdx], matrix[idx][n-1-jdx] = matrix[idx][n-1-jdx], matrix[idx][jdx]

