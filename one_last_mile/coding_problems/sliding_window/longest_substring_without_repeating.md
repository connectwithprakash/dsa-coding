# Longest Substring Without Repeating Characters

## Problem Statement
Given a string `s`, find the length of the longest substring without repeating characters.

## Examples
```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
```

## My Approach
I need to find the longest substring with all unique characters. My strategy uses a sliding window with two pointers:

- `idx` tracks the start of the current substring
- `jdx` tracks the end of the current substring
- Use a set to track characters in the current window

When I encounter a repeated character at `jdx`:
1. If it's the same as the character at `idx` → just move both pointers forward
2. If it's somewhere in the middle → remove all characters from `idx` up to (and including) the first occurrence of the repeated character

This ensures my window always contains unique characters.

## My Solution
```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Base case: strings with length < 2
        if len(s) < 2:
            return len(s)
        
        idx = 0  # Start of current substring
        n = len(s)
        jdx = 1  # End of current substring
        substring = set(s[idx])  # Characters in current window
        longest_substring_len = 1
        
        while (jdx < n):
            if s[jdx] in substring:
                # Found a repeated character
                if s[idx] == s[jdx]:
                    # Repeated char is at the start - move both pointers
                    idx += 1
                    jdx += 1
                else:
                    # Repeated char is in the middle - shrink window from left
                    while s[idx] != s[jdx]:
                        substring.remove(s[idx])
                        idx += 1
                    idx += 1  # Move past the repeated character
                    jdx += 1
            else:
                # New unique character - expand window
                substring.add(s[jdx])
                jdx += 1
            
            # Update max length after each operation
            longest_substring_len = max(longest_substring_len, (jdx-idx))
        
        return longest_substring_len
```

## Complexity Analysis ✅
- **Time Complexity**: O(n) - Each character is visited at most twice (once by `jdx`, once by `idx`)
- **Space Complexity**: O(m) where m = size of character set (at most 26 for lowercase, 128 for ASCII, etc.)

Meets the recommended complexity requirements!

## Example Walkthrough
**Input**: `s = "pwwkew"`

**Process**:
1. Start: `idx=0(p), jdx=1(w)`, set={p}, add 'w' → set={p,w}
2. `idx=0(p), jdx=2(w)`, 'w' repeated! → remove 'p', move idx to 2
3. `idx=2(w), jdx=3(k)`, set={w}, add 'k' → set={w,k}
4. `idx=2(w), jdx=4(e)`, add 'e' → set={w,k,e}, **length=3**
5. `idx=2(w), jdx=5(w)`, 'w' repeated! → move idx to 3
6. Continue...

**Maximum length**: 3 (substring "wke")

## What I Learned
- **Sliding window with set** - Perfect for tracking unique elements
- **Two types of repetition** - Character at start vs middle of window
- **Shrinking strategy** - Remove from left until we can include the new character
- **Each character visited at most twice** - Once by each pointer, ensuring O(n) time

## Alternative Cleaner Implementation
```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}  # Store last seen index of each character
        max_length = 0
        left = 0
        
        for right, char in enumerate(s):
            if char in char_index and char_index[char] >= left:
                # Character is repeated in current window
                left = char_index[char] + 1  # Move left past the repetition
            
            char_index[char] = right  # Update last seen index
            max_length = max(max_length, right - left + 1)
        
        return max_length
```

This uses a hashmap to store indices, making the window adjustment more direct.

## Key Insights
- **My solution correctly handles both repetition cases** - At start or in middle
- **The sliding window never shrinks unnecessarily** - Only when forced by repetition
- **Set operations are O(1)** - Making the overall algorithm efficient
- **The window always maintains the invariant** - All characters are unique