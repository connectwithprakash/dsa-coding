class Solution:
    def rotate(self, string: str, rotate_n_char: int) -> str:
        string = string[rotate_n_char:] + string[:rotate_n_char]
        return string

    def find_even_odd_len_palindrome(self, word_length, combinations, palindrome_indices, palindrome_word, even=False):
        if even:
            start = 4
        else:
            start = 5
        longest_palindrome_length = start - 2
        for palindrome_length in range(start, word_length + 1, 2):
            palindrome_new_indices = []
            for index in palindrome_indices:
                search_index = index - 1
                if search_index >= 0:
                    end_index = word_length-search_index
                    word = combinations[search_index][:end_index]
                    if (palindrome_length <= end_index) and (word[0] == word[palindrome_length-1]):
                        palindrome_new_indices.append(search_index)

            if len(palindrome_new_indices):
                palindrome_indices = palindrome_new_indices
                longest_palindrome_length = palindrome_length
            else:
                break

        return palindrome_indices[0], longest_palindrome_length

    def longestPalindrome(self, s: str) -> str:
        word_length = len(s)
        combinations = list(zip(*[self.rotate(s, i) for i in range(word_length)]))

        palindrome_indices = [index for index, word in enumerate(combinations[:word_length - 1]) if word[0] == word[1]]
        palindrome_new_indices = [index for index, word in enumerate(combinations[:word_length - 2]) if word[0] ==
                                  word[2]]

        even_palindrome_len = odd_palindrome_len = 0
        if len(palindrome_indices) != 0:
            even_palindrome = combinations[palindrome_indices[0]][:2]
            even_palindrome_index, even_palindrome_len = self.find_even_odd_len_palindrome(word_length, combinations,
                                                                           palindrome_indices,
                                                                even_palindrome, True)
        if len(palindrome_new_indices) != 0:
            odd_palindrome = combinations[palindrome_new_indices[0]][:3]
            odd_palindrome_index, odd_palindrome_len = self.find_even_odd_len_palindrome(word_length, combinations,
                                                                                        palindrome_new_indices,
                                                               odd_palindrome, False)
        if even_palindrome_len > odd_palindrome_len:
            palindrome_word = combinations[even_palindrome_index][:even_palindrome_len]
        elif odd_palindrome_len:
            palindrome_word = combinations[odd_palindrome_index][:odd_palindrome_len]
        else:
            palindrome_word = combinations[0][0]

        return ''.join(palindrome_word)
