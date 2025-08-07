# Longest Repeating Character Replacement

## Problem Statement
You are given a string `s` and an integer `k`. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most `k` times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

## Examples
```
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
```

## My Approach
I need to find the longest window where I can make all characters the same by replacing at most k characters. The key insight: **keep the most frequent character and replace all others**.

My strategy uses a sliding window:
- Track character frequencies in the current window
- A window is valid if: `(window_length - max_frequency) ≤ k`
- Expand window by moving right pointer
- If invalid (too many replacements needed), shrink from left
- Track the maximum valid window length

**Key insight**: We don't need to decide which characters to replace - just ensure the window can be made uniform with k changes by keeping the most frequent character.

## My Solution with Detailed Comments
```python
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Dictionary to track frequency of each character in current window
        counter = defaultdict(int)
        
        # Two pointers for sliding window
        idx = 0  # Left boundary of window
        jdx = 0  # Right boundary of window
        
        # Track the maximum valid window length found
        max_len = 0

        # Expand window by moving right pointer
        while jdx < len(s):
            # Add current character to window frequency count
            counter[s[jdx]] += 1
            
            # Calculate current window size
            # +1 because window is inclusive of both boundaries
            window_len = jdx - idx + 1
            
            # Find the character with maximum frequency in current window
            # This is the character we'll keep, replacing all others
            window_max_char = max(counter, key=counter.get)
            window_max_value = counter[window_max_char]

            # Check if current window is valid:
            # Can we make all chars the same with at most k replacements?
            if (window_len - window_max_value) <= k:
                # Valid window - update maximum length if this is longer
                max_len = max(max_len, window_len)
            else:
                # Invalid window - too many replacements needed
                # Shrink window from left by removing leftmost character
                counter[s[idx]] -= 1
                # Move left boundary right
                idx += 1
            
            # Always expand window to explore new possibilities
            jdx += 1
            
        return max_len
```

## Complexity Analysis ✅
- **Time Complexity**: O(n) - Each character is visited at most twice (once by each pointer)
- **Space Complexity**: O(1) - Dictionary can have at most 26 uppercase letters

## Example Walkthrough
**Input**: `s = "AABABBA"`, `k = 1`

**Process**:
1. Window "A": len=1, max_freq=1, need 0 replacements ✓
2. Window "AA": len=2, max_freq=2, need 0 replacements ✓
3. Window "AAB": len=3, max_freq=2(A), need 1 replacement ✓
4. Window "AABA": len=4, max_freq=3(A), need 1 replacement ✓
5. Window "AABAB": len=5, max_freq=3(A), need 2 replacements ✗ → shrink
6. Window "ABAB": len=4, max_freq=2, need 2 replacements ✗ → shrink
7. Continue sliding...

**Maximum length**: 4

## What I Learned
- **Sliding window doesn't always expand** - It contracts when invalid
- **Don't track which character to replace** - Just count frequencies
- **Keep the most frequent character** - Always optimal strategy
- **Window validity is simple** - Just check `(window_len - max_freq) ≤ k`
- **Finding max in dictionary** - Use `max(dict, key=dict.get)` pattern

## Alternative Optimization
Some solutions track `max_freq` globally without recalculating, but I find my approach clearer for understanding. The optimization doesn't change the complexity class.

```python
max_freq = 0
while jdx < len(s):
    counter[s[jdx]] += 1
    max_freq = max(max_freq, counter[s[jdx]])  # Only update, never decrease
    # Even if max_freq becomes stale, it doesn't affect correctness
```
This optimization works because we only care about windows that are larger than our current maximum, and a stale `max_freq` won't create false positives.