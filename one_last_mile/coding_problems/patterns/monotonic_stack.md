# Monotonic Stack Pattern

## What is a Monotonic Stack?
A stack that maintains elements in either strictly increasing or strictly decreasing order. When a new element breaks the monotonic property, we pop elements until the property is restored.

## When to Use This Pattern

### Problem Characteristics
- Finding the **next greater/smaller element**
- Finding the **previous greater/smaller element**  
- Problems involving **ranges** or **boundaries**
- Need to know "how many days/elements until X condition"
- Rectangle/histogram problems

### Keywords That Signal This Pattern
- "next greater"
- "next smaller"
- "previous greater"
- "previous smaller"
- "days until"
- "nearest"
- "maximum rectangle"
- "largest area"

## Core Concept

The key insight: **Elements in the stack represent "potential candidates" that haven't found their answer yet**.

When we pop elements, we're essentially saying "this new element is the answer you were waiting for".

## Two Types of Monotonic Stacks

### 1. Monotonic Decreasing Stack
- Used for finding **next greater element**
- Stack maintains: `stack[i] >= stack[i+1]`
- Pop when: current element > stack top

### 2. Monotonic Increasing Stack  
- Used for finding **next smaller element**
- Stack maintains: `stack[i] <= stack[i+1]`
- Pop when: current element < stack top

## Generic Template

```python
def monotonic_stack_pattern(array):
    stack = []  # Can store indices or (value, index) tuples
    result = [default_value] * len(array)
    
    for i, val in enumerate(array):
        # For decreasing stack (next greater)
        while stack and val > array[stack[-1]]:
            idx = stack.pop()
            result[idx] = i - idx  # or val, depending on problem
        
        stack.append(i)  # or (val, i)
    
    # Handle remaining elements in stack
    # These elements never found their "next greater"
    
    return result
```

## Problems I've Solved

### 1. Daily Temperatures
**Pattern**: Monotonic decreasing stack
**Key insight**: Track days waiting for warmer temperature
```python
# Stack stores (temperature, index)
while stack and current_temp > stack[-1][0]:
    # Found warmer day for stack top
    item = stack.pop()
    result[item[1]] = current_idx - item[1]
```

### 2. Largest Rectangle in Histogram  
**Pattern**: Monotonic increasing stack with index inheritance
**Key insight**: When popping, current bar can extend left to popped bar's position
```python
# Stack stores (leftmost_extension, height)
while stack and current_height < stack[-1][1]:
    left_idx, height = stack.pop()
    area = height * (current_idx - left_idx)
    # Current bar inherits left_idx
```

### 3. Next Greater Element Series
**Pattern**: Basic monotonic decreasing stack
**Key insight**: Elements waiting in stack haven't found their next greater

## Advanced Techniques

### Index Inheritance
When popping elements, the current element can "inherit" properties from popped elements:
```python
leftmost_idx = current_idx
while stack and current < stack[-1]:
    popped = stack.pop()
    leftmost_idx = popped.index  # Inherit
stack.append((leftmost_idx, current))
```

### Storing Tuples
Often useful to store both value and index:
```python
stack.append((value, index, additional_info))
```

### Circular Arrays
For circular next greater element:
```python
# Process array twice
for i in range(2 * n):
    actual_idx = i % n
    # Normal monotonic stack logic
```

## Complexity Analysis
- **Time**: O(n) - each element pushed and popped at most once
- **Space**: O(n) - stack can contain all elements in worst case

## Common Pitfalls

1. **Forgetting to process remaining stack** - Elements still in stack at the end need handling
2. **Wrong comparison** - Using > vs >= can change results
3. **Index vs Value confusion** - Be clear what you're storing
4. **Not tracking additional info** - Sometimes need more than just value

## Evolution from Brute Force

### Brute Force Approach
```python
# O(n²) - for each element, scan all following elements
for i in range(n):
    for j in range(i+1, n):
        if array[j] > array[i]:
            result[i] = j
            break
```

### Optimized with Monotonic Stack
```python
# O(n) - single pass with stack
for i in range(n):
    while stack and array[i] > array[stack[-1]]:
        idx = stack.pop()
        result[idx] = i
    stack.append(i)
```

## Visual Intuition

```
Array: [2, 1, 2, 4, 3]
Finding next greater element:

Step 1: Process 2
Stack: [2]
Result: [?, ?, ?, ?, ?]

Step 2: Process 1 (1 < 2, push)
Stack: [2, 1]
Result: [?, ?, ?, ?, ?]

Step 3: Process 2 (2 > 1, pop 1)
Stack: [2, 2]
Result: [?, 2, ?, ?, ?]

Step 4: Process 4 (4 > 2, pop both)
Stack: [4]
Result: [4, 2, 4, ?, ?]

Step 5: Process 3 (3 < 4, push)
Stack: [4, 3]
Result: [4, 2, 4, ?, ?]

Final: Remaining stack elements have no next greater
Result: [4, 2, 4, -1, -1]
```

## Related Patterns
- **Sliding Window Maximum** - Can use deque (similar to monotonic structure)
- **Heap problems** - When need min/max but not next element relationship
- **Dynamic Programming** - Some range problems combine with DP

## My Key Learnings

1. **"Next element" problems scream monotonic stack** - This is the #1 signal
2. **Stack represents waiting elements** - They're waiting for their answer
3. **Popping means "found the answer"** - The current element satisfies waiting elements
4. **Index tracking is crucial** - Often need to know positions, not just values
5. **Single pass is powerful** - O(n) solution for what seems like O(n²) problem