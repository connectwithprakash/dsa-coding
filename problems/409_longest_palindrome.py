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
