# Intuition
The idea was to have a hash map of the character counts of string `p` and then loop through the characters of `s` and if the char is from `p` then decrease its count value. Also, keep track of number of character already seen that forms anagram. If the size of character seen is equal to the length of anagram then I add the index and continue with the process until the last character.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
<!-- Describe your approach to solving the problem. -->
There are three cases we have to deal with. We store character count in `char_counts` variable. We use this variable to know if we are expecting the current character indexed in `s` to be in `p`. We loop through the characters in string `s` and handle the following situations.
1. Character at index `i` is required to form an anagram. So, in this case we increase the `anagram_count` variable and also decrease the required character count to form anagram.
2. Character at index `i` continues to form an anagram. Eg: In `s="abab"` and `p="ab"`, first `ab` is an anagram and then when at index `i=2` as well, `ba` is also an anagram. So in this case we find this character from start of anagram characters so that we can use use character at `i` inplace of that and the result would still be an anagram. In the example: we find `a` at `i=0`, remove it as seen from `char_count`. 
3. Character at index `i` is not a part of an anagram, then, we know that this is not a start of an anagram or a part of it. So we skip these characters.

# Complexity
- Time complexity: ~O(n)
<!-- Add your time complexity here, e.g. $$O(n)$$ --> 

- Space complexity: O(1)
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```
def get_counts(string):
    counts = {}
    for c in string:
        counts[c] = 0
    for c in string:
        counts[c] += 1

    return counts

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # Variable to hold the indices
        indices = []
        # get character chounts from string "p"
        char_counts = get_counts(p)
        # Create a temporary variable to modify when finding an anagram
        temp_counts = char_counts.copy()
        # Set length of string p to compare if we have got anagram or not
        len_p = len(p)
        # Holds the length of word that could be an anagram seen for comparison with p_len
        anagram_len = 0

        # Loop through the string "s" and see if we gor anagram
        for i in range(len(s)):
            # If count is zero means index i is the start of a possible anagram
            if not anagram_len:
                start = i
            # Check if current character forms anagram
            if temp_counts.get(s[i], 0):
                anagram_len += 1
                temp_counts[s[i]] -= 1
            # If the indexed character cannot form an anagram, two cases.
            else:
                # 1st case is that the character is a part of anagram but it's just that we don't need that character. In that case we try to find that character from the start of current anagram search so as that current char replaces it.
                if s[i] in temp_counts:
                    for j in range(start, i):
                        temp_counts[s[j]] += 1
                        anagram_len -= 1
                        if s[j] == s[i]:
                            temp_counts[s[j]] -= 1
                            anagram_len += 1
                            break
                    start = j+1
                # 2nd case is that the character is not a part of string "p". In that case, we start from beginning
                else:
                    temp_counts = char_counts.copy()
                    anagram_len = 0
            if anagram_len == len_p:
                temp_counts[s[start]] += 1
                indices.append(start)
                start += 1
                anagram_len -= 1

        return indices

```
