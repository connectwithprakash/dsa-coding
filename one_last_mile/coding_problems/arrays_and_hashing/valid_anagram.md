# Valid Anagram

## Problem Statement
Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

**Constraint**: `s` and `t` consist of lowercase English letters.

## Examples
```
Input: s = "anagram", t = "nagaram"
Output: true

Input: s = "rat", t = "car"
Output: false
```

## My Approach

### Initial Thoughts
I need to check if both strings have the same characters with the same frequencies. My first instinct is to use a hashmap to count character occurrences in the first string, then decrement counts as I iterate through the second string.

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        s_counter = {}
        for char in s:
            if char in s_counter:
                s_counter[char] += 1
            else:
                s_counter[char] = 1
        for char in t:
            if s_counter.get(char, 0):
                s_counter[char] -= 1
            else:
                return False
        for char, value in s_counter.items():
            if value > 0:
                return False
        return True
```

**Complexity**: O(n) time, O(n) space

### Optimized O(1) Space Solution
Wait! Since the constraint says we only have lowercase English letters, I can use a fixed-size array instead of a hashmap. The array will only need 26 slots (one for each letter), making it O(1) space!

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # For lowercase English letters only
        count = [0] * 26
        
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        
        return all(c == 0 for c in count)
```

**Complexity**: O(n) time, O(1) space (fixed array of 26)

**Why the ordinal approach is clever**: 
- `ord('a')` = 97, `ord('b')` = 98, etc.
- So `ord(char) - ord('a')` maps: 'a'→0, 'b'→1, ..., 'z'→25
- This gives us perfect array indexing without a hashmap!
- We can increment/decrement in one loop since we know lengths are equal

### Alternative: Sorting Approach
I could also sort both strings and compare them:
```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
```

**Complexity**: O(n log n) time, O(1) space (if we don't count the space used by sorting)

## Key Insights I Learned
- My initial hashmap approach works but uses O(n) space
- The constraint "lowercase English letters only" is a huge hint! It means I can use a fixed array[26] for O(1) space
- Always check string lengths first - if they're different, they can't be anagrams (early optimization)
- The fixed-size array approach is faster than hashmap due to no hashing overhead

## What I'll Remember
- When I see "lowercase English letters" or any fixed character set, think O(1) space with arrays
- For general Unicode strings, hashmap is still the best approach
- Sorting is simple but slower at O(n log n)