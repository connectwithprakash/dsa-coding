# First Attempt: Naive pythonic way
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(' ')[-1])


# Second Attempt: Non pythonic way
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        idx, jdx = -1, -1
        space_before = True
        for i in range(len(s)):
            if s[i] == ' ':
                space_before = True
            else:
                if space_before:
                    space_before = False
                    idx = i
                    jdx = idx
                else:
                    jdx = i
        return (jdx - idx)+1

