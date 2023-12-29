# Attempt 1: Pythonic solution
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])


# Attempt 2: Non-pythonic solution
class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)
        jdx = 0
        start_word = False
        res_s = ''
        for idx in range(n-1, -1, -1):
            if not start_word and s[idx] != ' ':
                start_word = True
                jdx = idx+1
            
            if start_word:
                if s[idx] == ' ':
                    start_word = False
                    res_s += s[idx+1:jdx] + ' '
                elif idx == 0:
                    start_word = False
                    res_s += s[:jdx] + ' '

        return res_s[:-1]

