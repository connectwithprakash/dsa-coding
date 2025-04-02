# Intuition
The problem of adding two binary numbers is similar to how we add decimal numbers by hand. We process digits from right to left, keeping track of any carry that needs to be added to the next position. The main difference is that we're working in base-2 instead of base-10, which simplifies the addition rules since we only deal with 0s and 1s.

# Approach
1. First, ensure we're working with the longer string as 'a' to simplify the logic
2. Process both strings from right to left, handling three main cases:
   - Both digits are 1 (result depends on carry)
   - Both digits are 0 (result depends on carry)
   - One digit is 1 and one is 0 (result depends on carry)
3. Keep track of carry bit throughout the addition
4. After processing the shorter string, handle remaining digits of the longer string
5. Finally, add an extra 1 if there's still a carry
6. Since we built the result from right to left, reverse it before returning

The key insight is handling the carry bit properly for each case:
- 1 + 1 = 10 (result: 0, carry: 1)
- 1 + 0 = 1 (result: 1, carry: 0)
- 0 + 0 = 0 (result: 0, carry: 0)
- With carry: add 1 to each of these cases

# Complexity
- Time complexity: $O(max(n,m))$
  - where n and m are the lengths of input strings
  - We process each digit once
  - The final reverse operation is also linear
  - String join operation is linear

- Space complexity: $O(max(n,m))$
  - We store the result in a list that will be at most one digit longer than the longer input string
  - No recursive calls or additional data structures are used
  - The space used is proportional to the length of the output

# Code
```python3 []
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Get lengths of input strings
        len_a, len_b = len(a), len(b)
        min_len = min(len_a, len_b)
        
        # Ensure 'a' is always the longer string for simpler processing
        if len_a == min_len:
            a, b = b, a
            len_a, len_b = len_b, len_a
        
        carry = False  # Track carry bit
        result = []    # Store result digits
        
        # Process digits from right to left for the length of shorter string
        for idx in range(min_len):
            # Get current digits from right to left
            digit_a = a[len_a-idx-1]
            digit_b = b[len_b-idx-1]
            
            # Case 1: Both digits are 1
            if digit_a == "1" and digit_b == "1":
                # If carry exists: 1 + 1 + 1 = 11 (append 1, carry stays 1)
                # If no carry: 1 + 1 = 10 (append 0, carry becomes 1)
                result.append("1" if carry else "0")
                carry = True
                
            # Case 2: Both digits are 0
            elif digit_a == "0" and digit_b == "0":
                # If carry exists: 0 + 0 + 1 = 1 (append 1, carry becomes 0)
                # If no carry: 0 + 0 = 0 (append 0, carry stays 0)
                result.append("1" if carry else "0")
                carry = False
                
            # Case 3: One digit is 1, other is 0
            else:
                # If carry exists: 1 + 0 + 1 = 10 (append 0, carry stays 1)
                # If no carry: 1 + 0 = 1 (append 1, carry stays 0)
                result.append("0" if carry else "1")
        
        # Process remaining digits of longer string 'a'
        idx = min_len
        while idx < len_a:
            digit = a[len_a-idx-1]
            if carry:
                if digit == "1":
                    # 1 + 1 = 10 (append 0, carry stays 1)
                    result.append("0")
                    carry = True
                else:
                    # 0 + 1 = 1 (append 1, carry becomes 0)
                    result.append("1")
                    carry = False
            else:
                # No carry, just append the digit as is
                result.append(digit)
            idx += 1
        
        # If there's still a carry after processing all digits
        # add it as the most significant bit
        if carry:
            result.append("1")
        
        # Reverse the result and join into a string
        # We built the result from right to left, so we need to reverse it
        return "".join(result[::-1])

```
