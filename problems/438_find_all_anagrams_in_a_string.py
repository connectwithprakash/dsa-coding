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

