class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i, j = len(s)-1, len(t)-1

        def get_next_char_index(string, index):
            count = 0
            non_pound_seen = False
            while (index > -1):
                if (string[index] != '#'):
                    if (count == 0):
                        break
                    else:
                        index -= 1
                        count -= 1
                        non_pound_seen = True
                else:
                    if non_pound_seen:
                        count = 1
                        non_pound_seen = False
                    else:
                        count += 1
                        index -= 1
            return index

        while (i>-1) and (j>-1):
            if (s[i] == '#'):
                i = get_next_char_index(s, i)
            if (t[j] == '#'):
                j = get_next_char_index(t, j)
            if s[i] == t[j]:
                i -= 1
                j -= 1
            else:
                break
        return (i == j)

