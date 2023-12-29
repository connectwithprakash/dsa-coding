# Attempt 1: Pythonic solution

class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])


# Attempt 2: Non-pythonic solution
class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)
        start_idx = 0
        start_word = False
        res_s = ''
        for i in range(n):
            if not start_word and s[i] != ' ':
                start_word = True
                start_idx = i
            
            if start_word:
                if s[i] == ' ':
                    start_word = False
                    res_s = s[start_idx:i] + ' ' + res_s
                elif i == n-1:
                    start_word = False
                    res_s = s[start_idx:] + ' ' + res_s

        return res_s[:-1]

