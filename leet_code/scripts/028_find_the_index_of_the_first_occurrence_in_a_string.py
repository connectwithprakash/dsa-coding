class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_len = len(needle)
        for i in range(len(haystack)):
            if (needle[0] == haystack[i]) and (needle == haystack[i:i+needle_len]):
                return i

        return -1

