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

# Attempt 2: Another (faster) approach with out using character O(n^2)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])

        first_row_zero = False
        first_col_zero = False

        # Check if the first col contains 0
        for idx in range(m):
            if matrix[idx][0] == 0:
                first_col_zero = True
                break
        # Check if the first row contains zero
        for jdx in range(n):
            if matrix[0][jdx] == 0:
                first_row_zero = True
                break
        # Check inner matrix for zeros
        for idx in range(m):
            for jdx in range(0, n):
                if matrix[idx][jdx] == 0:
                    # Set column of first row to zero
                    matrix[0][jdx] = 0
                    # Set row of first column to zero
                    matrix[idx][0] = 0
        
        # Fill inner matrix (except 1st row and 1st col) with zeros
        for idx in range(1, m):
            for jdx in range(1, n):
                if matrix[idx][0] == 0 or matrix[0][jdx] == 0:
                    matrix[idx][jdx] = 0
        # Fill the first row
        if first_col_zero:
            for idx in range(m):
                matrix[idx][0] = 0
        # Fill the first column
        if first_row_zero:
                matrix[0] = [0]*n

