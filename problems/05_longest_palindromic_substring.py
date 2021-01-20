class Solution:
    def rotate(self, string: str, rotate_n_char: int) -> str:
        string = string[rotate_n_char:] + string[:rotate_n_char]
        return string

    def find_even_odd_len_palindrome(self, word_length, combinations, palindrome_indices, palindrome_word, even=False):
        if even:
            start = 4
            step = 1
        else:
            start = 5
            step = 1
        for palindrome_length in range(start, word_length + 1, 2):
            palindrome_new_indices = []
            for index in palindrome_indices:
                new_index = index - step
                if (new_index >= 0) and (new_index <= word_length - palindrome_length) and (
                        index < word_length - step - 1):
                    pass
                else:
                    continue
                word = combinations[new_index]
                if word[0] == word[palindrome_length - 1]:
                    palindrome_new_indices.append(new_index)
            if len(palindrome_new_indices) > 0 and (palindrome_length <= word_length):
                palindrome_indices = palindrome_new_indices
                palindrome_word = combinations[palindrome_indices[0]][:palindrome_length]
            else:
                palindrome_word = combinations[palindrome_indices[0]][:palindrome_length - 2]
                break
        return ''.join(palindrome_word)

    def longestPalindrome(self, s: str) -> str:
        word_length = len(s)
        combinations = list(zip(*[self.rotate(s, i) for i in range(word_length)]))

        palindrome_indices = [index for index, word in enumerate(combinations[:word_length - 1]) if word[0] == word[1]]
        palindrome_new_indices = [index for index, word in enumerate(combinations[:word_length - 2]) if word[0] ==
                                  word[2]]

        even_palindrome = odd_palindrome = ''
        if len(palindrome_indices) != 0:
            even_palindrome = combinations[palindrome_indices[0]][:2]
            even_palindrome = self.find_even_odd_len_palindrome(word_length, combinations, palindrome_indices,
                                                                even_palindrome, True)
        if len(palindrome_new_indices) != 0:
            odd_palindrome = combinations[palindrome_new_indices[0]][:3]
            odd_palindrome = self.find_even_odd_len_palindrome(word_length, combinations, palindrome_new_indices,
                                                               odd_palindrome, False)

        if len(even_palindrome) > len(odd_palindrome):
            palindrome_word = even_palindrome
        elif len(odd_palindrome):
            palindrome_word = odd_palindrome
        else:
            palindrome_word = combinations[0][0]

        return palindrome_word
