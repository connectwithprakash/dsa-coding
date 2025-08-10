# Evaluate Reverse Polish Notation

## Problem Statement
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are `+`, `-`, `*`, and `/`. Each operand may be an integer or another expression.

**Note** that division between two integers should truncate toward zero.

It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a result, and there will not be any division by zero operation.

## Examples
```
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = (4 + 2) = 6

Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
```

## My Approach
Reverse Polish Notation (RPN) is perfect for stack-based evaluation. In RPN, operators come after their operands, so I can:

- Push operands onto a stack as I encounter them
- When I see an operator, pop the required operands, perform the operation, and push the result back
- The final result will be the only element left in the stack

My strategy uses:
- A stack to store operands and intermediate results
- A hashmap with lambda functions for clean operator handling
- Proper operand order (first popped is second operand, second popped is first operand)

**Key insight**: Stack naturally handles the "most recent operands" requirement of RPN evaluation.

## My Solution with Detailed Comments
```python
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Map operators to their corresponding lambda functions
        # Note: char_x is first operand, char_y is second operand (due to stack LIFO)
        operations = {
            '+': lambda char_x, char_y: int(char_x) + int(char_y),
            '-': lambda char_x, char_y: int(char_x) - int(char_y),
            '*': lambda char_x, char_y: int(char_x) * int(char_y),
            '/': lambda char_x, char_y: int(int(char_x) / int(char_y))  # Truncates toward zero
        }
        stack = []
        
        for token in tokens:
            if token in operations:
                # Pop two operands (order matters for - and /)
                char_y = stack.pop()  # Second operand (most recent)
                char_x = stack.pop()  # First operand
                
                # Apply the operation and push result back to stack
                func = operations[token]
                result = func(char_x, char_y)
                stack.append(str(result))  # Store as string for consistency
            else:
                # Token is an operand, push to stack
                stack.append(token)
    
        # Final result is the only element left in stack
        return int(stack[0])
```

## Complexity Analysis
- **Time Complexity**: O(n) where n is the length of tokens - each token processed once
- **Space Complexity**: O(n) for the stack - worst case when all tokens are operands

## Example Walkthrough
**Input**: `tokens = ["2","1","+","3","*"]`

1. **"2"**: Operand → stack: `["2"]`
2. **"1"**: Operand → stack: `["2", "1"]`
3. **"+"**: Operator → pop "1", pop "2", compute 2+1=3 → stack: `["3"]`
4. **"3"**: Operand → stack: `["3", "3"]`
5. **"*"**: Operator → pop "3", pop "3", compute 3*3=9 → stack: `["9"]`
6. **Result**: `int(stack[0]) = 9`

**Input**: `tokens = ["4","13","5","/","+"]`

1. **"4"**: stack: `["4"]`
2. **"13"**: stack: `["4", "13"]`
3. **"5"**: stack: `["4", "13", "5"]`
4. **"/"**: pop "5", pop "13", compute 13/5=2 → stack: `["4", "2"]`
5. **"+"**: pop "2", pop "4", compute 4+2=6 → stack: `["6"]`
6. **Result**: `6`

## What I Learned
- **RPN evaluation pattern** - Stack-based approach is natural for postfix notation
- **Lambda functions in hashmaps** - Clean way to map operators to functions
- **Operand order importance** - First pop is second operand, second pop is first operand
- **String to int conversions** - Handle mixed string/int operations carefully
- **Division truncation** - Python's `int()` handles "truncate toward zero" correctly for this problem

## Key Implementation Details
- **Stack operations** - Push operands, pop for operators, push results
- **Operator precedence** - Not needed in RPN since operators come after operands
- **Result consistency** - Store intermediate results as strings to match input format
- **Edge cases** - Problem guarantees valid expressions, so no error handling needed
- **Final result** - Single element remaining in stack after processing all tokens