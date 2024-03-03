class Solution:
    def longestPalindrome(self, s: str) -> str:
        m = n = len(s)
        start_idx = 0
        longest_length = 1
        
        # DP table with palindrome of length 1 check
        dp = [[1 if (i==j) else 0 for j in range(n)] for i in range(m)]
        # Palindrome of length 2
        for i in range(m-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = 1
                start_idx = i
                longest_length = 2
        
        # For palindrome of length 3 and greater
        for j in range(2, n):
            for i in range(j-1):
                if (s[i] == s[j]) and (dp[i+1][j-1] == 1):
                    dp[i][j] = 1
                    length = (j-i) + 1
                    if length > longest_length:
                        longest_length = length
                        start_idx = i

        return s[start_idx:start_idx+longest_length]

