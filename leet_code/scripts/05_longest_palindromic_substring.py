def find_even_odd_len_palindrome(palindrome_indices, string, palindrome_word, even=False):
    if even:
        start = 4
    else:
        start = 5
    string_length = len(string)
    for palindrome_length in range(start, string_length + 1, 2):
        palindrome_new_indices = []
        for index in palindrome_indices:
            search_index = index - 1
            end_index = search_index + palindrome_length
            if (search_index >= 0) and (end_index <= string_length):
                word = string[search_index:end_index]
                if (word[0] == word[-1]):
                    palindrome_new_indices.append(search_index)

        if len(palindrome_new_indices):
            palindrome_indices = palindrome_new_indices
            start = palindrome_indices[0]
            end = start + palindrome_length
            palindrome_word = string[start:end]
        else:
            break

    return palindrome_word


class Solution:

    def longestPalindrome(self, string: str) -> str:
        word_length = len(string)

        even_palindrome_indices = [index for index in range(word_length-1) if string[index] == string[index+1]]
        odd_palindrome_indices = [index for index in range(word_length-2) if string[index] == string[index+2]]

        even_palindrome = odd_palindrome = ''
        if len(even_palindrome_indices) != 0:
            index = even_palindrome_indices[0]
            even_palindrome = string[index:index+2]
            even_palindrome = find_even_odd_len_palindrome(even_palindrome_indices, string, even_palindrome, True)
        if len(odd_palindrome_indices) != 0:
            index = odd_palindrome_indices[0]
            odd_palindrome = string[index:index + 3]
            odd_palindrome = find_even_odd_len_palindrome(odd_palindrome_indices, string, odd_palindrome, False)
        if len(even_palindrome) > len(odd_palindrome):
            return even_palindrome
        elif len(odd_palindrome):
            return odd_palindrome
        else:
            return string[0]