"""
# Length of longest palindrome

# Intuition
The problem seemed to be finding what charactes are repeated and create a palindrome out of it.

# Approach
Create a hash map to store the count of character that we have already seen. We loop through the characters in the string. We check if we have already seen that character and increase the count in either cases. We also see if the character has been repeated two times. If yes, we add it to the palindrome list and reset the count to zero.

At last, we look into hast map and see if there is any character that has been repeated just one time. If yes, we return the longest palindrome length as two times the length of repeated characters plus one, else, just two times the length of repeated characters.

# Complexity
- Time complexity: $$O(n)$$

- Space complexity: $$O(1)$$
"""

class Solution:
    def longestPalindrome(self, s: str) -> int:
        hash_map = {}
        palindrome = []
        for char in s:
            if char in hash_map:
                hash_map[char] += 1
            else:
                hash_map[char] = 1

            if (hash_map[char] == 2):
                palindrome.append(char)
                hash_map[char] = 0
            
        for k in hash_map:
            if (hash_map[k] == 1):
                return 2*len(palindrome)+1
        return 2*len(palindrome)


if __name__ == "__main__":
	sol = Solution()
	assert sol.longestPalindrome("abccccdd") == 7
	assert sol.longestPalindrome("a") == 1
