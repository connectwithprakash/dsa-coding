# Encode and Decode Strings

## Problem Statement
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

**Constraint**: `strs[i]` contains only UTF-8 characters.

## Examples
```
Input: ["lint","code","love","you"]
Output: ["lint","code","love","you"]
Explanation: One possible encode method is: "lint:;code:;love:;you"

Input: ["we", "say", ":", "yes"]
Output: ["we", "say", ":", "yes"]
Explanation: One possible encode method is: "we:;say:;:::;yes"
```

## My Approach Evolution

### ❌ First Attempt: Simple Separator
Use a delimiter character to join strings and split them back.
**Problem**: What if the delimiter appears in the strings themselves?

### ❌ Second Attempt: Non-UTF8 Character  
Use `chr(128)` as separator since it's outside UTF-8 range.
**Problem**: Still feels brittle and not elegant.

### ✅ Final Solution: Length + Separator Pattern
Use the format `"length#string"` for each string. This way, even if `#` appears in the string, I know exactly how many characters to read.

**Key insight**: The separator can appear in the string content, but it doesn't matter because I'm reading exactly the specified number of characters!

## My Solution
```python
class Solution:

    def encode(self, strs: List[str]) -> str:
        #  ["neet","code","love","you"]
        escape_char = '#'
        encoded_str = ''.join([f"{len(str_)}{escape_char}{str_}" for str_ in strs])
        # 4#neet4#code4#love3#you
        return encoded_str

    def decode(self, s: str) -> List[str]:
        idx = 0
        last_idx = 0
        m = len(s)
        escape_char = '#'
        result = []
        
        while idx < m:
            # Find the escape character to get length
            while s[idx] != escape_char:
                idx += 1
            
            # Extract the length of the string
            str_len = int(s[last_idx:idx])
            
            # Move past the escape char
            idx += 1
            
            # Extract exactly str_len characters
            result.append(s[idx:idx+str_len])
            
            # Move to next position
            idx = idx + str_len
            last_idx = idx
            
        return result
```

## Why This Works (Even with '#' in strings!)

**Example**: `["ab#c", "def"]` 
- **Encoded**: `"4#ab#c3#def"`
- **Decoding process**:
  1. Read until first `#` → length = `4`
  2. Read exactly 4 characters after `#` → `"ab#c"` ✅
  3. Continue from position after those 4 characters
  4. Read until next `#` → length = `3` 
  5. Read exactly 3 characters → `"def"` ✅

The magic is that I'm reading **exactly** the specified number of characters, so internal separators don't break the parsing!

## Complexity Analysis
- **Encode Time**: O(m) where m = sum of all string lengths
- **Decode Time**: O(m) single pass through encoded string  
- **Space**: O(m + n) where n = number of strings (for length prefixes)

## What I Learned
- **Length-prefixed encoding** is a fundamental technique in data serialization
- When separators can appear in data, use length information to determine boundaries
- The separator character doesn't need to be "safe" - the length tells us exactly what to read
- This pattern is used in many real protocols (HTTP headers, binary formats, etc.)

## Alternative Approaches I Considered

### Non-UTF8 Separator (Works but less elegant)
```python
def encode(self, strs: List[str]) -> str:
    sep = chr(257)  # Outside UTF-8 range
    return sep.join(strs)

def decode(self, s: str) -> List[str]:
    sep = chr(257)
    return s.split(sep)
```

### Escape Sequences (Too complex)
Escape special characters in the strings themselves - like JSON/XML escaping.

## Key Insight
My length + separator approach is the **standard solution** because:
- Robust: Handles any content in strings
- Efficient: O(m) time complexity
- Simple: Clean encode/decode logic
- Universal: Used in real-world protocols