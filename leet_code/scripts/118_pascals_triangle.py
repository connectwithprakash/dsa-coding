class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = []
        for i in range(numRows):
            row_val = []
            for j in range(i+1):
                if (j == 0) or (j == i):
                    row_val.append(1)
                else:
                    val = output[i-1][j-1] + output[i-1][j]
                    row_val.append(val)
            output.append(row_val)

        return output

