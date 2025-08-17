# Two Pointers Pattern

## What is Two Pointers?
A technique using two pointers to traverse data, often from different positions or directions. The pointers move based on problem logic, reducing what would be nested loops into a single pass.

## When to Use This Pattern

### Problem Characteristics
- Working with **sorted** arrays or linked lists
- Finding pairs with certain properties
- Palindrome verification
- Merging or comparing sequences
- Optimization problems with greedy choices

### Keywords That Signal This Pattern
- "sorted array"
- "pair" or "triplet"
- "palindrome"
- "two sum" (in sorted array)
- "merge"
- "reverse"
- "remove duplicates"
- "container" or "area"

## Types of Two Pointer Approaches

### 1. Opposite Direction (Converging)
Start from both ends, move toward center.

**When to use**:
- Palindrome checking
- Two sum in sorted array
- Container/area problems

**Template**:
```python
def opposite_pointers(arr):
    left = 0
    right = len(arr) - 1
    
    while left < right:
        if condition_met(arr[left], arr[right]):
            process_result()
        elif need_larger:
            left += 1
        else:
            right -= 1
    
    return result
```

### 2. Same Direction (Fast & Slow)
Both pointers move in same direction at different speeds.

**When to use**:
- Remove duplicates
- Linked list cycle detection
- Finding middle element

**Template**:
```python
def same_direction(arr):
    slow = 0
    fast = 0
    
    while fast < len(arr):
        if condition(arr[fast]):
            arr[slow] = arr[fast]
            slow += 1
        fast += 1
    
    return slow
```

### 3. Sliding/Expanding
One pointer fixed while other expands, then move fixed pointer.

**When to use**:
- Finding all pairs/triplets
- Substring problems (overlaps with sliding window)

## Problems I've Solved

### 1. Two Sum II (Sorted Array)
**Pattern**: Opposite direction
**Key insight**: If sum too small, move left; if too large, move right
```python
while left < right:
    current_sum = numbers[left] + numbers[right]
    if current_sum == target:
        return [left + 1, right + 1]
    elif current_sum < target:
        left += 1  # Need larger sum
    else:
        right -= 1  # Need smaller sum
```

### 2. 3Sum
**Pattern**: Fix one pointer, use two pointers for remaining
**Key insight**: Sort first, then reduce to 2Sum problem
```python
for i in range(len(nums) - 2):
    # Skip duplicates
    if i > 0 and nums[i] == nums[i-1]:
        continue
    
    # Two pointers for remaining array
    left, right = i + 1, len(nums) - 1
    while left < right:
        total = nums[i] + nums[left] + nums[right]
        # Standard two pointer logic
```

### 3. Container With Most Water
**Pattern**: Opposite direction with greedy choice
**Key insight**: Always move the pointer with smaller height
```python
while left < right:
    area = min(heights[left], heights[right]) * (right - left)
    max_area = max(max_area, area)
    
    # Move pointer with smaller height (limiting factor)
    if heights[left] < heights[right]:
        left += 1
    else:
        right -= 1
```

### 4. Valid Palindrome
**Pattern**: Opposite direction with character filtering
**Key insight**: Skip non-alphanumeric, compare case-insensitive
```python
while left < right:
    # Skip non-alphanumeric
    while left < right and not s[left].isalnum():
        left += 1
    while left < right and not s[right].isalnum():
        right -= 1
    
    # Compare
    if s[left].lower() != s[right].lower():
        return False
```

### 5. Trapping Rain Water
**Pattern**: Two pointers with running max
**Key insight**: Water level determined by smaller of two boundaries
```python
while left < right:
    if left_max <= right_max:
        water += max(0, left_max - height[left])
        left_max = max(left_max, height[left])
        left += 1
    else:
        water += max(0, right_max - height[right])
        right_max = max(right_max, height[right])
        right -= 1
```

## Advanced Techniques

### Multiple Pointer Sets
For k-sum problems:
```python
def kSum(nums, target, k):
    if k == 2:
        return twoSum(nums, target)
    
    result = []
    for i in range(len(nums) - k + 1):
        # Recursively reduce to (k-1)-sum
        sub_result = kSum(nums[i+1:], target - nums[i], k - 1)
```

### Pointer with Binary Search
Sometimes combine two pointers with binary search:
```python
for i in range(n):
    for j in range(i+1, n):
        # Binary search for third element
        target = -(nums[i] + nums[j])
        idx = binary_search(nums, j+1, n-1, target)
```

### Greedy Pointer Movement
Decision on which pointer to move based on optimization:
```python
# Container With Most Water example
# Always move the shorter line - it's the limiting factor
if height[left] < height[right]:
    left += 1
else:
    right -= 1
```

## Complexity Analysis
- **Time**: Usually O(n) for single pass, O(n²) if nested
- **Space**: Usually O(1) extra space (not counting output)

## Common Pitfalls

1. **Forgetting to handle duplicates** - Often need to skip duplicate values
2. **Infinite loops** - Ensure pointers actually move
3. **Off-by-one errors** - Be clear about inclusive/exclusive bounds
4. **Not sorting first** - Many two-pointer problems require sorted input

## Evolution from Brute Force

### Brute Force (Nested Loops)
```python
# O(n²) - Check all pairs
for i in range(n):
    for j in range(i+1, n):
        if condition(arr[i], arr[j]):
            process()
```

### Two Pointers Optimization
```python
# O(n) - Single pass with two pointers
left, right = 0, n-1
while left < right:
    if condition(arr[left], arr[right]):
        process()
    # Move pointers based on logic
```

## Visual Intuition

```
Array: [1, 2, 3, 4, 5, 6, 7]
Finding pair that sums to 9:

Step 1: left=1, right=7, sum=8 (too small, move left)
        ^             ^

Step 2: left=2, right=7, sum=9 (found!)
           ^          ^

Container with Most Water:
Heights: [1, 8, 6, 2, 5, 4, 8, 3, 7]

Step 1: left=1, right=7, area=1*8=8
        ^                         ^

Step 2: left=8, right=7 (move shorter pointer)
           ^                      ^
```

## When to Choose Two Pointers vs Other Patterns

### Use Two Pointers When:
- Array is sorted or can be sorted
- Need to find pairs/triplets
- Problem has greedy property
- Linear scan is sufficient

### Consider Alternatives When:
- Need to track complex state → Sliding Window
- Non-contiguous elements → Dynamic Programming
- Need all combinations → Backtracking
- Unsorted and can't sort → Hash Map

## My Key Learnings

1. **Sorting often enables two pointers** - O(n log n) sort + O(n) scan beats O(n²) brute force
2. **Pointer movement logic is crucial** - Must guarantee progress and termination
3. **Greedy choices often work** - Like moving shorter height in Container problem
4. **Reduce k-sum to 2-sum** - Powerful technique for multiple element problems
5. **Skip duplicates early** - Prevents duplicate results in output

## Related Patterns
- **Sliding Window** - Special case where pointers maintain a range
- **Binary Search** - Sometimes combined for 3+ element problems
- **Fast & Slow Pointers** - For cycle detection in linked lists