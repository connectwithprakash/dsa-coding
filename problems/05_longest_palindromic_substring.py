class Solution:
    def rotate(self, string: str, rotate_n_char: int) -> str:
        return string[rotate_n_char:] + string[:rotate_n_char]

    def is_palindrome(self, s: str) -> bool:
        print(s)
        if len(s) == 0:
            return False
        else:
            return s == ''.join(reversed(list(s)))

    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        indices, palindromes, lengths = [], [], []

        for i in range(0, n):
            if self.is_palindrome(s[i-1:i+2]):
                indices.append(i)

        for i in indices:
            j = 1
            while 2*j+1 <= n:
                word = s[i-j:i+j+1]
                if self.is_palindrome(word):
                    j += 1
                else:
                    break

            palindromes.append(s[i-j+1:i+j])
            lengths.append(2*j+1)
        return palindromes[lengths.index(max(lengths))]
