class Solution:
    def rotate(self, string: str, rotate_n_char: int) -> str:
        string = string[rotate_n_char:] + string[:rotate_n_char]
        return string

    def is_palindrome(self, s: str) -> bool:
        s1 = ''.join(s)
        s2 = ''.join(reversed(s))
        return s1 == s2

    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if s == ''.join(reversed(list(s))):
            return s
        for i in reversed(range(1, n)):
            combinations = list(zip(*[self.rotate(s, j) for j in range(i)]))
            index = n-i+1
            combinations = combinations[:index]
            has_palindromes = [self.is_palindrome(word) for word in combinations]
            if True in has_palindromes:
                return ''.join(combinations[has_palindromes.index(True)])
