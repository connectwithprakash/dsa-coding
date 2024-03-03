class Solution:
    def isPalindrome(self, s: str) -> bool:
        idx, jdx = 0, len(s)-1
        s = s.lower()
        while idx <= jdx:
            if not s[idx].isalnum():
                idx += 1
                continue

            if not s[jdx].isalnum():
                jdx -= 1
                continue

            if s[idx] != s[jdx]:
                return False
            else:
                idx += 1
                jdx -= 1

        return True

