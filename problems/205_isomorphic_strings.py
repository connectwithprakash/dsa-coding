# Attempt 2
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashmap = {}
        for idx in range(len(s)):
            if s[idx] in hashmap:
                if hashmap[s[idx]] != t[idx]:
                    return False
            else:
                if t[idx] not in hashmap.values():
                    hashmap[s[idx]] = t[idx]
                else:
                    return False

        return True

