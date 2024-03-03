# Solution 1: O(n^2) time complexity and O(n) space complexity

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        head = idx = longest_len_count = 0
        seen_letters = []
        total_length = len(s)
        longest_substring_len = 0
        
        while idx != total_length:
            letter = s[idx]
            if letter not in seen_letters:
                seen_letters.append(letter)
                substring_len = len(s[head:idx+1])
                idx += 1
                longest_len_count += 1
            else:
                seen_letters = seen_letters[1:]
                substring_len = len(s[head:idx])
                longest_len_count = 0
                head += 1
                
            if substring_len > longest_substring_len:
                longest_substring_len = substring_len
        
        return longest_substring_len
        

# Solution 2: O(n^2) time complexity and O(n) space complexity

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        head, tail = 0, 0
        max_len = (len(s) & True)

        for tail in range(len(s)):
            if s[tail] in s[head:tail]:
                substring_len = (tail - head)
                while (s[head] != s[tail]):
                    head += 1
                head += 1
            else:
                substring_len = ((tail + 1) - head)
            if substring_len > max_len:
                max_len = substring_len

        return max_len

# Attempt 3: O(n^2) solution
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        idx, jdx = 0, 0
        n = len(s)
        longest_substring_len = 0
        while jdx < n:
            if s[jdx] in s[idx:jdx]:
                while s[idx] != s[jdx]:
                    idx+= 1
                idx += 1
            else:
                jdx += 1
                
            if (jdx-idx) > longest_substring_len:
                longest_substring_len = (jdx-idx)

        return longest_substring_len

