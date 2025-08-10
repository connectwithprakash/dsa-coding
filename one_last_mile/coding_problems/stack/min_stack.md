# Min Stack

## Problem Statement
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the `MinStack` class:
- `MinStack()` initializes the stack object.
- `void push(int val)` pushes the element `val` onto the stack.
- `void pop()` removes the element on the top of the stack.
- `int top()` gets the top element of the stack.
- `int getMin()` retrieves the minimum element in the stack.

You must implement a solution with O(1) time complexity for each function.

## Examples
```
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
```

## My Approach
The challenge is maintaining the minimum element in O(1) time while supporting stack operations. The key insight: **each element should remember the minimum value that existed up to that point in the stack**.

My strategy:
- Store each element as a tuple: `(value, min_so_far)`
- When pushing: compare new value with current minimum and store the smaller one
- When popping: the remaining stack automatically has the correct minimum
- All operations become O(1) since we store the minimum with each element

**Key insight**: Instead of recalculating the minimum each time, pre-compute and store it with each element.

## My Solution with Detailed Comments
```python
class MinStack:

    def __init__(self):
        # Stack will store tuples of (value, min_up_to_this_point)
        self.stack = []
        
    def push(self, val: int) -> None:
        # If stack has elements, compare val with current minimum
        if len(self.stack):
            current_min = self.stack[-1][1]  # Get current minimum
            new_min = min(current_min, val)  # Find new minimum
            self.stack.append((val, new_min))
        else:
            # First element - it's both the value and the minimum
            self.stack.append((val, val))

    def pop(self) -> None:
        # Standard pop operation - remove top element
        # The remaining stack automatically has correct minimum stored
        self.stack.pop()

    def top(self) -> int:
        # Return the actual value (first element of tuple)
        return self.stack[-1][0]

    def getMin(self) -> int:
        # Return the minimum (second element of tuple)  
        # This is the minimum of all elements currently in stack
        return self.stack[-1][1]
```

## Complexity Analysis
- **Time Complexity**: O(1) for all operations - no loops or recursive calls
- **Space Complexity**: O(n) where n is number of elements - storing one tuple per element

## Example Walkthrough
**Operations**: `push(-2), push(0), push(-3), getMin(), pop(), top(), getMin()`

1. **push(-2)**: Stack empty → store `(-2, -2)` → Stack: `[(-2, -2)]`
2. **push(0)**: min(-2, 0) = -2 → store `(0, -2)` → Stack: `[(-2, -2), (0, -2)]`
3. **push(-3)**: min(-2, -3) = -3 → store `(-3, -3)` → Stack: `[(-2, -2), (0, -2), (-3, -3)]`
4. **getMin()**: Return `stack[-1][1] = -3`
5. **pop()**: Remove `(-3, -3)` → Stack: `[(-2, -2), (0, -2)]`
6. **top()**: Return `stack[-1][0] = 0`
7. **getMin()**: Return `stack[-1][1] = -2`

## What I Learned
- **Auxiliary information storage** - Store additional data with each element to optimize queries
- **Pre-computation strategy** - Calculate and store results instead of computing on-demand
- **Tuple usage in stacks** - Effective way to bundle related information
- **Stack context preservation** - Each level remembers its own state
- **Space-time tradeoff** - Use O(n) extra space to achieve O(1) time operations

## Alternative Approaches
1. **Two stacks**: Separate stack for minimums, but requires careful synchronization
2. **Single variable**: Track global minimum, but fails when minimum element is popped

My tuple approach is cleaner and handles all edge cases naturally.

## Key Implementation Details
- **Tuple structure**: `(actual_value, minimum_up_to_this_element)`
- **First element handling**: When stack is empty, element is both value and minimum
- **Minimum propagation**: Each new element compares with previous minimum
- **Automatic cleanup**: Popping elements automatically restores correct minimum context