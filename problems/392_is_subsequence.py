class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j = 0
        s_len = len(s)
        for i in range(len(t)):
            if j < s_len and s[j] == t[i]:
                j += 1
        return (j == s_len)

