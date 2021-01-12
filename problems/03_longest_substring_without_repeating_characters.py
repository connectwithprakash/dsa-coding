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
        
        # # Testing window method
        # max_len = 0
        # for i in range(1, len(s)+1):
        #     for j in range(0, len(s)-i+1):
        #         substring = s[j:j+i]
        #         substring_len = len(substring)
        #         if len(set(substring)) == substring_len:
        #             if substring_len>max_len:
        #                 max_len = substring_len
        # return max_len
