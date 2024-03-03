# Attempt 1: Naive O(n^2) solution
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped_anagrams = []
        n = len(strs)
        idx, jdx = 0, 1

        def is_valid_anagram(s, t):
            hashmap = {}
            if len(s) != len(t):
                return False
            # Create a hashmap of the character count
            for char in s:
                if hashmap.get(char, 0):
                    hashmap[char] += 1
                else:
                    hashmap[char] = 1
            # Find if the string is an anagram checking if the char
            # is present in the hashmap
            for char in t:
                if hashmap.get(char, 0):
                    hashmap[char] -= 1
                else:
                    return False

            return True

        grouped_anagrams = []
        visited = []
        for idx in range(n):
            anagrams = []
            if idx in visited:
                continue
            for jdx in range(idx+1, n):
                if jdx in visited:
                    continue
                elif is_valid_anagram(strs[idx], strs[jdx]):
                    anagrams.append(strs[jdx])
                    visited.append(jdx)
            visited.append(idx)
            anagrams.append(strs[idx])
            grouped_anagrams.append(anagrams)

        return grouped_anagrams


# Attempt 2: O(n*mlog(m)) solution
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:    
        grouped_anagrams = {}
        for idx in range(len(strs)):
            sorted_word = ''.join(sorted(strs[idx]))
            if not grouped_anagrams.get(sorted_word, 0):
                grouped_anagrams[sorted_word] = []
            
            grouped_anagrams[sorted_word].append(strs[idx])
        grouped_anagrams = list(grouped_anagrams.values())

        return grouped_anagrams

