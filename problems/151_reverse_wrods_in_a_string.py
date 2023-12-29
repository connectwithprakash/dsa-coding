# Attempt 1: Pythonic solution

class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])


# Attempt 2: Non-pythonic solution
class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)
        start_idx = n
        stop_idx = n
        word_start = False
        res_lst = []
        for i in range(n-1, -1, -1):
            print(i)
            if not word_start and s[i] != ' ':
                print(f"word start at {i} -> {s[i]}")
                word_start = True
                start_idx = i
                stop_idx = i+1
            elif word_start:
                if s[i] == ' ':
                    word_start = False
                    print(f"word end at {i} -> {s[i+1]}")
                    start_idx = i + 1
                elif i == 0:
                    word_start = False
                    start_idx = 0
                else:
                    start_idx = i
                
                if not word_start:
                    res_lst.append(s[start_idx:stop_idx])

        if word_start:
            res_lst.append(s[start_idx:stop_idx])

        return ' '.join(res_lst)


        
        return res_s

