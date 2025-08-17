# Minimum Window Substring

## Problem Statement
Given two strings `s` and `t` of lengths `m` and `n` respectively, return the minimum window substring of `s` such that every character in `t` (including duplicates) is included in the window. If there is no such substring, return the empty string `""`.

The testcases will be generated such that the answer is unique.

## Examples
```
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" inclAudes 'A', 'B', and 'C' from string t.

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
```

## My Approach
I need to find the smallest substring in `s` that contains all characters from `t` (with their frequencies). This is a variable-size sliding window problem.

My strategy uses two pointers:
- Expand window by moving `jdx` until all characters from `t` are covered
- Once valid, shrink window by moving `idx` while maintaining validity
- Track the minimum valid window during contraction
- Continue until we've explored all possible windows

**Key insight**: Use frequency matching - the window must contain at least the required count of each character from `t`, but can have extras.

## My Solution with Detailed Comments
```python
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) == 1 and s == t:
            return s
            
        idx, jdx = 0, 0  # Two pointers for sliding window
        s_counter = defaultdict(int)  # Track character frequencies in current window
        t_counter = defaultdict(int)  # Track required character frequencies
        
        # Build frequency map for target string t
        for char in t:
            t_counter[char] += 1

        # Helper function to check if current window contains all characters of t
        # Window is valid if it has at least the required count for each character
        def contains(counter_a, counter_b):
            return all([True if (counter_a[key] >= counter_b[key]) else False for key in counter_b.keys()])

        min_win_substring = None
        
        # Expand window by moving right pointer
        while (jdx < len(s)):
            # Add current character to window
            s_counter[s[jdx]] += 1
            
            # While window is valid, try to shrink it to find minimum
            while contains(s_counter, t_counter):
                # Current window is valid - check if it's the smallest so far
                string = s[idx:jdx+1]
                if (min_win_substring is None) or (len(string) < len(min_win_substring)):
                    min_win_substring = string
                
                # Shrink window from left by removing leftmost character
                s_counter[s[idx]] -= 1
                idx += 1
            
            # Expand window for next iteration
            jdx += 1

        return min_win_substring if min_win_substring is not None else ""
```

## Complexity Analysis
- **Time Complexity**: O(n) where n = len(s) - each character visited at most twice by the two pointers
- **Space Complexity**: O(1) - at most 52 letters (uppercase + lowercase) in dictionaries

## Example Walkthrough
**Input**: `s = "ADOBECODEBANC"`, `t = "ABC"`

1. Build `t_counter = {A:1, B:1, C:1}`
2. Expand window: A, D, O, B, E, C → window "ADOBEC" contains all of ABC
3. Shrink while valid: "ADOBEC" → "DOBEC" → "OBEC" → invalid
4. Continue expanding: "OBECOD" → "OBECODE" → "OBECODEB" → "OBECODEBA" → "OBECODEBANC"
5. When window contains ABC again, shrink: "BANC" is smaller than "ADOBEC"
6. Final answer: "BANC"

## What I Learned
- **Variable-size sliding window** - Expand until valid, then contract while valid
- **Frequency matching** - Check if window has at least required counts, not exact matches
- **Nested while loops** - Outer expands, inner contracts efficiently
- **String slicing for result** - Use `s[idx:jdx+1]` to get current window
- **Two-pointer technique** - Each character processed at most twice for O(n) time

## Key Implementation Details
- **Initialization**: Both pointers start at 0, expand first pointer immediately
- **Window validity**: Use helper function to compare frequency dictionaries
- **Minimum tracking**: Update minimum only when window is valid and smaller
- **Edge case**: Handle single character strings separately
- **Return format**: Empty string if no valid window exists