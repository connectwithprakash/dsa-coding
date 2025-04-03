class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # common_prefix = ""
        #         for i in range(min_len):
        #             char = strs[0][i]
        #             for string in strs:
        #                 if char != string[i]:
        #                     return common_prefix
        #             common_prefix += char

        #         return common_prefix

        # Another approach
        # Start with the first string as the initial prefix
        common_prefix = strs[0]

        # Compare the prefix with each string in the list
        for s in strs[1:]:
            # Reduce the prefix until it matches the start of the current string
            while not s.startswith(common_prefix):
                common_prefix = common_prefix[:-1]
                if not common_prefix:
                    return ""

        return common_prefix
