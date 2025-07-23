# Group Anagrams

## Problem Statement
Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

## Examples
```
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Input: strs = [""]
Output: [[""]]

Input: strs = ["a"]
Output: [["a"]]
```

## My Approach
I need to group strings that are anagrams of each other. Two strings are anagrams if they have the same character frequencies. My strategy:

1. For each string, create a "signature" representing its character counts
2. Use this signature as a key in a hashmap  
3. Group all strings with the same signature together
4. Return all the groups

Since we're dealing with lowercase English letters, I can use the ordinal value trick with a fixed array[26] to count characters efficiently.

## My Solution
```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def get_count(string: str) -> List[int]:
            counter = [0]*26
            for char in string:
                counter[ord(char)- ord('a')] += 1
            return counter

        hash_map = {}
        for string in strs:
            char_count = get_count(string)
            char_count = str(char_count)  # Convert to string for hashability
            if char_count in hash_map:
                hash_map[char_count].append(string)
            else:
                hash_map[char_count] = [string]

        return [val for _, val in hash_map.items()]
```

## Complexity Analysis
- **Time Complexity**: O(n * m) where n = number of strings, m = average string length
- **Space Complexity**: O(n * m) for storing all strings in groups

## What I Learned
- Character frequency counting is more efficient than sorting for this problem
- Converting arrays to strings makes them hashable (though tuple would be more efficient)
- The ordinal value approach `ord(char) - ord('a')` gives perfect array indexing
- Using a helper function makes the code cleaner and more readable

## Alternative Approaches I Considered

### Sorting Approach
```python
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    hash_map = {}
    for string in strs:
        sorted_str = ''.join(sorted(string))
        if sorted_str in hash_map:
            hash_map[sorted_str].append(string)
        else:
            hash_map[sorted_str] = [string]
    return list(hash_map.values())
```
**Complexity**: O(n * m log m) time - Slower due to sorting each string

### Optimized Versions of My Approach

**Using tuple instead of string:**
```python
char_count = tuple(char_count)  # More efficient than str()
```

**Using defaultdict to eliminate if-else:**
```python
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def get_count(string: str) -> tuple:
            counter = [0]*26
            for char in string:
                counter[ord(char)- ord('a')] += 1
            return tuple(counter)

        hash_map = defaultdict(list)
        for string in strs:
            char_count = get_count(string)
            hash_map[char_count].append(string)  # No need for if-else!

        return list(hash_map.values())
```

## Key Insight
My character counting approach is actually optimal! It's faster than sorting because:
- Counting: O(m) per string
- Sorting: O(m log m) per string
- Both approaches have the same space complexity