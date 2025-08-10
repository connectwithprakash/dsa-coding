# Valid Parentheses

## Problem Statement
Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

## Examples
```
Input: s = "()"
Output: true

Input: s = "()[]{}"
Output: true

Input: s = "(]"
Output: false

Input: s = "([)]"
Output: false

Input: s = "{[]}"
Output: true
```

## My Approach
I need to track opening brackets and match them with their corresponding closing brackets in the correct order. This is a perfect use case for a **stack data structure**.

My strategy:
- Use a stack to track opening brackets as I encounter them
- Use a hashmap to map each closing bracket to its corresponding opening bracket
- When I encounter a closing bracket, pop from stack and verify it matches
- At the end, the stack should be empty for valid parentheses

**Key insight**: The stack naturally handles the "correct order" requirement - the most recent unmatched opening bracket should match the current closing bracket.

## My Solution with Detailed Comments
```python
class Solution:
    def isValid(self, s: str) -> bool:
        # Map each closing bracket to its corresponding opening bracket
        parantheses = {
            ']': '[',
            '}': '{',
            ')': '('
        }
        stack = []
        
        for char in s:
            # If current character is a closing bracket
            if char in parantheses:
                # Check if stack is not empty AND popped element matches expected opening bracket
                if len(stack) and (stack.pop() == parantheses[char]):
                    continue  # Valid match, continue processing
                else:
                    return False  # Either empty stack or mismatch
            else:
                # Current character is opening bracket, push to stack
                stack.append(char)
        
        # Valid only if all opening brackets have been matched (empty stack)
        return False if len(stack) else True
```

## Complexity Analysis
- **Time Complexity**: O(n) where n is the length of the string - each character processed once
- **Space Complexity**: O(n) in worst case when all characters are opening brackets

## Example Walkthrough
**Input**: `s = "{[]}"`

1. **'{'**: Opening bracket → push to stack: `['{']`
2. **'['**: Opening bracket → push to stack: `['{', '[']`
3. **']'**: Closing bracket → pop `'['`, matches `parantheses[']'] = '['` ✓ → stack: `['{']`
4. **'}'**: Closing bracket → pop `'{'`, matches `parantheses['}'] = '{'` ✓ → stack: `[]`
5. **End**: Stack is empty → return `True`

**Input**: `s = "([)]"`

1. **'('**: Opening bracket → stack: `['(']`
2. **'['**: Opening bracket → stack: `['(', '[']`
3. **')'**: Closing bracket → pop `'['`, but `parantheses[')'] = '('` ≠ `'['` ✗ → return `False`

## What I Learned
- **Stack for nested structures** - Perfect for tracking opening brackets in correct order
- **Hashmap for fast lookups** - Map closing to opening brackets for O(1) validation
- **Edge case handling** - Always check if stack is empty before popping
- **Condition chaining** - Use `and` to ensure both conditions are met before proceeding
- **Final validation** - Empty stack indicates all brackets were properly matched

## Key Implementation Details
- **HashMap design** - Closing brackets as keys, opening brackets as values for easy lookup
- **Stack operations** - Push opening brackets, pop and validate on closing brackets
- **Early termination** - Return false immediately on mismatch or empty stack violation
- **Final check** - Stack must be empty for valid parentheses string