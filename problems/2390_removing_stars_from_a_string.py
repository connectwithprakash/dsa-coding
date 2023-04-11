# Attempt 1: Solution similar to "Backspace String Compare".
class Solution:
    def removeStars(self, s: str) -> str:
        j = len(s) - 1
        output = []
        count = 0
        while (j >= 0):
            if (s[j] == "*"):
                while (s[j] == "*"):
                    count += 1
                    j -= 1
                while count:
                    if (s[j] == "*"):
                        break
                    j -= 1
                    count -= 1
            else:
                output.append(s[j])
                j -= 1
        return "".join(output[::-1])

