class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = min(len(string) for string in strs)
        common_prefix = ""
        for i in range(min_len):
            char = strs[0][i]
            for string in strs:
                if char != string[i]:
                    return common_prefix
            common_prefix += char
        
        return common_prefix

