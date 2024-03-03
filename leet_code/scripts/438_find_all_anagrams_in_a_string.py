"""
# Brute-force naive O(n^2) solution

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        indices = []
        p_map = {}
        for c in p:
            p_map[c] = 0
        for c in p:
            p_map[c] += 1

        for i in range(len(s)-len(p)+1):
            temp_p_map = p_map.copy()
            found = True
            for j in range(len(p)):
                if temp_p_map.get(s[i+j], 0):
                    temp_p_map[s[i+j]] -= 1
                else:
                    found = False
                    break
            if found:
                indices.append(i)
        return indices
"""

# Sliding window using two pointers

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        indices = []
        p_map = {}
        for c in p:
            p_map[c] = 0
        for c in p:
            p_map[c] += 1
        temp_p_map = p_map.copy()
        len_p = len(p)
        count = 0
        for i in range(len(s)):
            if not count:
                start = i
            if temp_p_map.get(s[i], 0):
                count += 1
                temp_p_map[s[i]] -= 1
            else:
                if s[i] in temp_p_map:
                    for j in range(start, i):
                        temp_p_map[s[j]] += 1
                        count -= 1
                        if s[j] == s[i]:
                            temp_p_map[s[j]] -= 1
                            count += 1
                            break
                    start = j+1
                else:
                    temp_p_map = p_map.copy()
                    count = 0
            if count == len_p:
                temp_p_map[s[start]] += 1
                indices.append(start)
                start += 1
                count -= 1

        return indices

