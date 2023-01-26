class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        char_map = {}
        for i in range(len(s)):
            if s[i] not in char_map:
                if t[i] in char_map.values():
                    return False
                else:
                    char_map[s[i]] = t[i]
            else:
                if char_map[s[i]] != t[i]:
                    return False
        return True
