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

            if not zigzag:
                data[idx].append(char)
                idx += 1
            elif zigzag:
                data[idx].append(char)
                idx -= 1

        for i in range(numRows):
            data[i] = "".join(data[i])

        return "".join(data)


# Second attempt: slightly faster execution time (minor change)
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        data = ['' for _ in range(numRows)]
        idx = 0
        zigzag = False

        for char in s:
            if idx == numRows:
                zigzag = True
                idx -= 2
            if idx == 0:
                zigzag = False

            if not zigzag:
                data[idx] += char
                idx += 1
            elif zigzag:
                data[idx] += char
                idx -= 1

        return "".join(data)

