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

