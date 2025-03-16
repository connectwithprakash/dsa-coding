"""
Input: Matrix of numbers
Output: Array with numbers ordering in diagonal traversal manner
Idea: An iead would be to get a list of dynamic list where we store
all the diagonal element from first 0 to n_rows and then from n_rows+1
to n_cols, basically to move across the L shape and store the diagonal
of each of them. Then as a second step, flip the elements of the array
of the array at 1 skip.T: O(n*k), S: O(n*k)
"""


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        results = []
        m, n = len(mat), len(mat[0])
        # Top to bottom
        for kdx in range(m):
            idx = kdx
            jdx = 0
            diag_elements = []
            while idx >= 0 and jdx < n:
                diag_elements.append(mat[idx][jdx])
                idx -= 1
                jdx += 1
            results.append(diag_elements)
        # left to right
        for kdx in range(1, n):
            idx = m - 1
            jdx = kdx
            diag_elements = []
            while jdx < n and idx >= 0:
                diag_elements.append(mat[idx][jdx])
                idx -= 1
                jdx += 1
            results.append(diag_elements)
        # Correct the ordering
        n_diags = len(results)
        result = []
        for idx in range(n_diags):
            if idx % 2:  # flip the numbers
                for jdx in range(len(results[idx])):
                    result.append(results[idx].pop())
            else:  # don't flip
                result.extend(results[idx])

        return result
