# Attempt 1
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        data = [[] for _ in range(numRows)]
        idx = 0
        zigzag = False

        for char in s:
            if idx == numRows:
                zigzag = True
                idx -= 2
            if idx == 0:
                zigzag = False

            if idx >= 0 and not zigzag:
                data[idx].append(char)
                idx += 1
            elif zigzag and idx > 0:
                data[idx].append(char)
                idx -= 1

        for i in range(numRows):
            data[i] = "".join(data[i])
        return "".join(data)

