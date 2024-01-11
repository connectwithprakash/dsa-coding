# Attempt 1: Naive Approach
# 1. Change the value of zeros to some char
# 2. Look for the position with this char
# 3. Traverse Row and Column of this position
# 4. Set the value to zero.

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])

        def traverse(idx, jdx):
            # Set row zeros
            for ldx in range(n):
                if matrix[idx][ldx] != 'z':
                    matrix[idx][ldx] = 0
            # Set column
            for kdx in range(m):
                if matrix[kdx][jdx] != 'z':
                    matrix[kdx][jdx] = 0
        # Set zeros to some other value for identification
        for idx in range(m):
            for jdx in range(n):
                if matrix[idx][jdx] == 0:
                    matrix[idx][jdx] = 'z'
        # Iterate through the matrix and make zero
        for idx in range(m):
            for jdx in range(n):
                if matrix[idx][jdx] == 'z':
                    traverse(idx, jdx)
                    matrix[idx][jdx] = 0

