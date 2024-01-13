# Attempt: O(n) using hashmap
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap = {}
        # Create a count of char in magazine
        for char in magazine:
            if hashmap.get(char, 0):
                hashmap[char] += 1
            else:
                hashmap[char] = 1

        # Check if the char from ransomNote is available in magazine
        for char in ransomNote:
            if hashmap.get(char, 0):
                hashmap[char] -= 1
            else:
                return False

        return True

