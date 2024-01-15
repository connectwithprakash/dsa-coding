# Attempt 1: O(n) solution using hashmap
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}
        if len(s) != len(t):
            return False
        
        for char in s:
            if hashmap.get(char, 0):
                hashmap[char] += 1
            else:
                hashmap[char] = 1

        for char in t:
            if hashmap.get(char, 0):
                hashmap[char] -= 1
            else:
                return False

        return True

