class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        prev_row_vals = []
        for i in range(rowIndex+1):
            curr_row_vals = []
            for j in range(i+1):
                if (j == 0) or (i == j):
                    curr_row_vals.append(1)
                else:
                    val = prev_row_vals[j-1] + prev_row_vals[j]
                    curr_row_vals.append(val)
            prev_row_vals = curr_row_vals

        return prev_row_vals

