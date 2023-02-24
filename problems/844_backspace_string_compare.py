"""
# O(n) time and space complexity solution
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def get_text(text: str) -> str:
            cursor = 0
            text = list(text)
            for i in range(len(text)):
                if text[i] != '#':
                    text[cursor] = text[i]
                    cursor += 1
                else:
                    cursor = max(0, cursor-1)
            return "".join(text[:cursor])

        s = get_text(s)
        t = get_text(t)

        return (s==t)

"""

# O(n) time complexity and O(1) space complexity

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def get_next_index(string, index):
            count = 0
            while (index > -1):
                if string[index] != '#':
                    if (count > 0):
                        index -= 1
                        count -= 1
                    else:
                        break
                else:
                    count += 1
                    index -= 1

            return index
        
        i, j = len(s)-1, len(t)-1
        while True:
            i = get_next_index(s, i)
            j = get_next_index(t, j)
            if ((i > -1) and (j >= -1)) and (s[i] == t[j]):
                i -= 1
                j -= 1
            else:
                break
        return ((i == -1) and (j == -1))

