# Permutation in String

## Problem Statement
Given two strings `s1` and `s2`, return `true` if `s2` contains a permutation of `s1`, or `false` otherwise.

In other words, return `true` if one of `s1`'s permutations is a substring of `s2`.

## Examples
```
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains "ba", which is a permutation of "ab".

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
Explanation: s2 does not contain any permutation of "ab".
```

## My Approach
I need to check if any substring of `s2` contains a permutation of `s1`. The key insight: **permutations have identical character frequencies**.

My strategy uses a **fixed-size sliding window**:
- Window size equals `len(s1)`
- Track character frequencies in both `s1` and the current window
- Slide the window through `s2`, updating frequencies incrementally
- If frequencies match, we found a permutation

**Key insight**: Instead of generating all permutations (factorial time!), I just compare character frequencies since any permutation has the same counts.

## My Solution with Detailed Comments
```python
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Count character frequencies in s1 (the pattern we're looking for)
        s1_counter = defaultdict(int)
        # Count character frequencies in current window of s2
        s2_counter = defaultdict(int)
        
        # Build frequency map for s1
        for char in s1:
            s1_counter[char] += 1
        
        s1_len = len(s1)
        s2_len = len(s2)
        idx = 0  # Left boundary of sliding window
        
        # Helper function to check if two frequency maps match
        # Only need to check keys in s1_counter since those are what matter
        def matches(d1, d2):
            for key in d1.keys():
                if d1[key] != d2[key]:
                    return False
            return True

        # Slide window through s2
        for jdx in range(0, s2_len):
            # Add current character to window
            s2_counter[s2[jdx]] += 1
            
            # If window size exceeds s1 length, shrink from left
            # Using sum of values to track window size
            if sum(s2_counter.values()) > s1_len:
                # Remove leftmost character from window
                s2_counter[s2[idx]] -= 1
                # Move left boundary right
                idx += 1
            
            # Check if current window is a permutation of s1
            if matches(s1_counter, s2_counter):
                return True

        return False
```

## Complexity Analysis ✅
- **Time Complexity**: O(n) where n is the length of `s2` - each character visited once
- **Space Complexity**: O(1) - at most 26 lowercase letters in dictionaries

## Example Walkthrough
**Input**: `s1 = "ab"`, `s2 = "eidbaooo"`

1. Build `s1_counter = {a:1, b:1}`
2. Window "e": `{e:1}` → no match
3. Window "ei": `{e:1, i:1}` → no match  
4. Window "eid": size > 2, shrink to "id": `{i:1, d:1}` → no match
5. Window "idb": size > 2, shrink to "db": `{d:1, b:1}` → no match
6. Window "dba": size > 2, shrink to "ba": `{b:1, a:1}` → **MATCH!**

**Result**: `true`

## What I Learned
- **Permutation = frequency matching** - Don't generate permutations, just compare counts
- **Fixed-size window** - Perfect for checking specific-length substrings
- **Incremental updates** - Add/remove one character at a time
- **Only check relevant keys** - The `matches` function only validates `s1`'s characters

## Optimized Solution
After reviewing my initial solution, I realized some optimizations:
- **Window size tracking with `sum()`** is inefficient - called every iteration
- **Zero counts not cleaned up** - could affect dictionary comparison
- **Can initialize the first window** before starting the slide

```python
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
            
        s1_counter = defaultdict(int)
        s2_counter = defaultdict(int)
        
        # Count s1 frequencies
        for char in s1:
            s1_counter[char] += 1
        
        # Initialize first window completely
        for i in range(len(s1)):
            s2_counter[s2[i]] += 1
        
        # Check if first window matches
        if s1_counter == s2_counter:
            return True
        
        # Slide the window
        for i in range(len(s1), len(s2)):
            # Add new character entering window
            s2_counter[s2[i]] += 1
            
            # Remove character leaving window
            old_char = s2[i - len(s1)]
            s2_counter[old_char] -= 1
            if s2_counter[old_char] == 0:
                del s2_counter[old_char]  # Clean up zero counts
            
            # Check match with direct dictionary comparison
            if s1_counter == s2_counter:
                return True
        
        return False
```

**Key improvements:**
1. **Early termination** - Return false if `s1` longer than `s2`
2. **Fixed window initialization** - Build first window before sliding
3. **Direct dictionary comparison** - More efficient than custom `matches()`
4. **Zero count cleanup** - Ensures accurate comparison
5. **No window size tracking** - We know it's always `len(s1)`

## Alternative Array Approach
Since only lowercase letters are allowed, I could use fixed arrays:
```python
# Use arrays for O(1) space (26 lowercase letters)
s1_count = [0] * 26
window_count = [0] * 26

# Count frequencies using ord(char) - ord('a') as index
# Compare with s1_count == window_count directly
```

My dictionary approach is more intuitive, but arrays offer slightly better performance.