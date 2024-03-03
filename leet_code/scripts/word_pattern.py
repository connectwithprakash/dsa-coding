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


# Attempt 2: Using double hashmapt to remove the computation
# of hashmap.values() in each step - Faster solution - O(n^2)
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        word2pattern = {}
        pattern2word = {}
        if len(pattern) != len(words):
            return False
        
        for idx in range(len(words)):
            if not word2pattern.get(words[idx], 0):
                if not pattern2word.get(pattern[idx], 0):
                    word2pattern[words[idx]] = pattern[idx]
                    pattern2word[pattern[idx]] = words[idx]
                else:
                    return False
            else:
                if word2pattern[words[idx]] != pattern[idx]:
                    return False
        return True

