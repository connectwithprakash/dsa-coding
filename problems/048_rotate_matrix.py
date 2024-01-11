# Attempt 1: Transpose and Flip the Matrix Approach (slightly faster solution than the attempt 2)
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


# Attempt 2: Both transpose and flip in the same loop (slightly slower solution)
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        mid_point = n/2
        for idx in range(m):
            for jdx in range(n):
                # Transpose the matrix
                if jdx >= idx:
                    matrix[idx][jdx], matrix[jdx][idx] = matrix[jdx][idx], matrix[idx][jdx]
                # Flip the matrix
                if jdx >= mid_point:
                    matrix[idx][jdx], matrix[idx][n-1-jdx] = matrix[idx][n-1-jdx], matrix[idx][jdx]

