class Solution:
    def rotate(self, string: str, rotate_n_char: int) -> str:
        string = string[rotate_n_char:] + string[:rotate_n_char]
        return string

    def is_palindrome(self, s: str) -> bool:
        s1 = ''.join(s)
        s2 = ''.join(reversed(s))
        return s1 == s2

    def longestPalindrome(self, s: str) -> str:
        word_length = len(s)
        combinations = list(zip(*[self.rotate(s, i) for i in range(word_length)]))
        for palindrome_length in reversed(range(1, word_length+1)): # for word lengths 1...n
            has_palindromes = [self.is_palindrome(chars_tuple[:palindrome_length]) for chars_tuple in combinations[
                                                                                                      :word_length-palindrome_length+1]]
            if True in has_palindromes:
                longest_palindrome = combinations[:word_length-palindrome_length+1][has_palindromes.index(True)]
                return ''.join(longest_palindrome[:palindrome_length])
