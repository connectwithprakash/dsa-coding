class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i, j = len(s)-1, len(t)-1

        def get_next_char_index(string, index):
            count = 0
            while (index > -1) and (string[index] == '#'):
                if string[index-1] == '#':
                    count += 1
                    index -= 1
                else:
                    index -= 2
            print('next -> ',string, index, count)
            return (index - count)

        while (i>-1) and (j>-1):
            if (s[i] == '#') or (t[j] == '#'):
                i = get_next_char_index(s, i)
                j = get_next_char_index(t, j)
                print(i, j)
            elif s[i] == t[j]:
                i -= 1
                j -= 1
            else:
                break
        return (i == j)

