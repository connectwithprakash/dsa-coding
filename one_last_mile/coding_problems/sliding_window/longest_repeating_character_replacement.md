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

## My Intuition
After struggling with this problem, I realized the key insight: **we want to find the longest window where we can make all characters the same by replacing at most k characters**.

The core idea that finally clicked for me:
- In any window, we keep the most frequent character and replace all others
- If (window_length - count_of_most_frequent_char) ≤ k, the window is valid
- We can transform this window into all same characters with at most k replacements

## Thought Process to Solve

### Step 1: Identify the Pattern
This is a sliding window problem because:
- We're looking for a substring (contiguous)
- We need to optimize for the longest valid substring
- There's a constraint (k replacements) that determines validity

### Step 2: The Key Formula
For any window to be valid:
```
replacements_needed = window_length - most_frequent_char_count
valid_window = (replacements_needed <= k)
```

### Step 3: Window Management Strategy
1. **Expand**: Always try to expand the window by moving right pointer
2. **Check validity**: After expansion, check if window is still valid
3. **Contract if needed**: If invalid, shrink from left by one position
4. **Track maximum**: Keep track of the longest valid window seen

### Step 4: Why This Works
- We're essentially asking: "Can I make this window uniform with k changes?"
- The most efficient way is to keep the most frequent character and change everything else
- As we slide the window, we're exploring all possible substrings

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
- **The sliding window doesn't always expand** - It contracts when invalid
- **We don't need to track which character to replace** - Just count frequencies
- **The "most frequent character" strategy** - Always optimal to keep the most common one
- **Window validity check is simple** - Just one inequality to check
- **Finding max in dictionary** - Use `max(dict, key=dict.get)` pattern

## Key Insights That Helped Me
1. **Don't overthink which characters to replace** - The math handles it automatically
2. **The window size formula is inclusive** - Remember the +1 for `jdx - idx + 1`
3. **We shrink by exactly one** - Not a while loop, just one character at a time
4. **Track the maximum throughout** - Not just at the end

## Alternative Optimization
Some solutions track `max_freq` globally without recalculating, but I find my approach clearer for understanding. The optimization doesn't change the complexity class.