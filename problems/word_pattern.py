# Attempt 1: Using single hashmap
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        hashmap = {}
        if len(pattern) != len(words):
            return False
        
        for idx in range(len(words)):
            if words[idx] not in hashmap:
                if pattern[idx] not in hashmap.values():
                    hashmap[words[idx]] = pattern[idx]
                else:
                    return False
            else:
                if hashmap[words[idx]] != pattern[idx]:
                    return False
        return True

