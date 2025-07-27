# Valid Palindrome

## Problem Statement
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.

## Examples
```
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
```

## My Approach
I need to check if the string is a palindrome considering only alphanumeric characters. My strategy uses **two pointers**:

1. **Start from both ends** - Left pointer at beginning, right pointer at end
2. **Skip non-alphanumeric characters** - Move pointers inward when encountering non-alphanumeric chars
3. **Compare characters** - When both pointers point to alphanumeric chars, compare them
4. **Early termination** - Return false immediately if characters don't match

**Key insight**: Instead of creating a new string, I can skip invalid characters on the fly!

## My Solution
```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        idx, jdx = 0, len(s)
        while idx < jdx:
            if not s[idx].isalnum():
                idx += 1
                continue
            if not s[jdx-1].isalnum():
                jdx -= 1
                continue
            
            if (s[idx] == s[jdx-1]):
                idx += 1
                jdx -= 1
                continue
            else:
                return False

        return True
```

## Complexity Analysis ✅
- **Time Complexity**: O(n) - Single pass through the string with two pointers
- **Space Complexity**: O(1) - Only using two pointer variables, no extra space

**Perfect! Meets both requirements** ✅

## Example Walkthrough
**Input**: `s = "A man, a plan, a canal: Panama"`
**After lowercase**: `"a man, a plan, a canal: panama"`

**Two-pointer process**:
1. `idx=0 ('a'), jdx=30 ('a')` → Match! Move both pointers
2. `idx=1 (' '), jdx=29 ('m')` → Skip space, `idx=2`
3. `idx=2 ('m'), jdx=29 ('m')` → Match! Move both pointers
4. `idx=3 ('a'), jdx=28 ('a')` → Match! Move both pointers
5. `idx=4 ('n'), jdx=27 ('n')` → Match! Move both pointers
...continue until pointers meet...

**Result**: All comparisons match → `true` ✅

## What I Learned
- **Two-pointer technique**: Efficient for palindrome checking without extra space
- **Character validation**: `isalnum()` method for checking alphanumeric characters  
- **In-place processing**: Skip invalid characters instead of preprocessing the string
- **Early termination**: Return false immediately on first mismatch for efficiency

## Alternative Approaches I Considered

### Preprocessing Approach (Higher Space Complexity)
```python
def isPalindrome(self, s: str) -> bool:
    # Clean the string first
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]
```
**Issue**: O(n) extra space for the cleaned string

### Recursive Approach
```python
def isPalindrome(self, s: str) -> bool:
    def helper(left, right):
        if left >= right:
            return True
        
        # Skip non-alphanumeric from left
        while left < right and not s[left].isalnum():
            left += 1
        # Skip non-alphanumeric from right  
        while left < right and not s[right].isalnum():
            right -= 1
            
        if s[left].lower() != s[right].lower():
            return False
            
        return helper(left + 1, right - 1)
    
    return helper(0, len(s) - 1)
```
**Issue**: O(n) space due to recursion stack

## Key Insights
- **My iterative two-pointer approach is optimal** for this problem
- **Skipping characters on-the-fly** avoids preprocessing overhead
- **Single pass solution** with constant space is the best we can achieve
- **Early termination** makes it efficient in practice

