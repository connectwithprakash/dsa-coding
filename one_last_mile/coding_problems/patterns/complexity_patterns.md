# Complexity Patterns Guide

## Common Time Complexity Patterns

### O(1) - Constant Time
**Common Operations:**
- Array access by index
- HashMap get/put (average case)
- Push/pop from stack
- Basic arithmetic operations

**Example Problems:**
- Min Stack operations (all O(1))
- Get Random from array

### O(log n) - Logarithmic Time
**Common Patterns:**
- Binary Search
- Balanced tree operations
- Heap push/pop operations

**Key Insight:** Eliminating half of remaining elements each step

### O(n) - Linear Time
**Common Patterns:**
- Single pass through array
- Two pointers (single traversal)
- Sliding window
- Monotonic stack (amortized)
- Building frequency map

**Key Insight:** Each element processed constant number of times

### O(n log n) - Linearithmic Time
**Common Patterns:**
- Sorting (merge sort, heap sort)
- Building a heap from array
- Processing n elements with log n operation each

**Example Problems:**
- 3Sum (sort + O(n²) traversal)
- Car Fleet (sort + O(n) traversal)

### O(n²) - Quadratic Time
**Common Patterns:**
- Nested loops over array
- Checking all pairs
- Dynamic programming with 2D table

**Example Problems:**
- 3Sum (after sorting)
- Brute force two sum

### O(2ⁿ) - Exponential Time
**Common Patterns:**
- Recursive solutions without memoization
- Generating all subsets
- Backtracking without pruning

**When Acceptable:** Small input size (n < 20)

## Space Complexity Patterns

### O(1) - Constant Space
**Techniques:**
- Two pointers without extra storage
- Modifying input array in-place
- Using fixed-size arrays (e.g., 26 for lowercase letters)

**Example:**
```python
# Two Sum II with sorted array
def twoSum(numbers, target):
    left, right = 0, len(numbers) - 1
    # Only using two variables, O(1) space
```

### O(n) - Linear Space
**Common Causes:**
- HashMap/Set storing n elements
- Stack/Queue with n elements
- Recursion depth of n
- Creating new array for result

**Example:**
```python
# Valid Parentheses
def isValid(s):
    stack = []  # Worst case: all opening brackets
    # O(n) space
```

### O(k) - K-Dependent Space
**When It Appears:**
- Sliding window of size k
- Heap maintaining k elements
- HashMap with at most k distinct keys

**Example:**
```python
# Sliding Window Maximum
def maxSlidingWindow(nums, k):
    heap = []  # At most k elements
    # O(k) space
```

## Amortized Analysis

### What is Amortized Time?
Average time per operation over a sequence of operations.

### Common Amortized O(1) Operations
1. **Dynamic Array Append**
   - Usually O(1), occasionally O(n) for resize
   - Amortized O(1)

2. **Monotonic Stack**
   - Each element pushed and popped once
   - Total O(n) for n elements = Amortized O(1) per element

### Example: Daily Temperatures
```python
def dailyTemperatures(temperatures):
    stack = []
    for temp in temperatures:
        while stack and temp > stack[-1][0]:
            stack.pop()  # Each element popped at most once
        stack.append(temp)
    # Looks like O(n²) but actually O(n) amortized
```

## Pattern-Specific Complexities

### Sliding Window
- **Fixed window**: O(n) time, O(1) or O(k) space
- **Variable window**: O(n) time, O(min(n, alphabet)) space

### Two Pointers
- **Single pass**: O(n) time, O(1) space
- **With sorting**: O(n log n) time, O(1) space

### Monotonic Stack
- **Time**: O(n) amortized - each element pushed/popped once
- **Space**: O(n) worst case - all elements in stack

### Frequency Counting
- **Time**: O(n) to build frequency map
- **Space**: O(k) where k is distinct elements

### Prefix/Suffix Arrays
- **Build time**: O(n)
- **Query time**: O(1)
- **Space**: O(n) for arrays

## Optimization Techniques

### Trading Space for Time
```python
# Brute Force: O(n²) time, O(1) space
def twoSum_brute(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

# Optimized: O(n) time, O(n) space
def twoSum_optimized(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        if target - num in seen:
            return [seen[target - num], i]
        seen[num] = i
```

### Early Termination
```python
# Can terminate early when optimal solution found
def maxProfit(prices):
    if len(prices) < 2:
        return 0  # Early termination
```

### Preprocessing for Multiple Queries
```python
class RangeSum:
    def __init__(self, nums):
        # O(n) preprocessing
        self.prefix = [0]
        for num in nums:
            self.prefix.append(self.prefix[-1] + num)
    
    def query(self, i, j):
        # O(1) per query
        return self.prefix[j+1] - self.prefix[i]
```

## Complexity Analysis Tips

### 1. Count Nested Loops
- Single loop: O(n)
- Two nested: O(n²)
- Three nested: O(n³)

### 2. Recursive Complexity
```python
def recursive(n):
    if n <= 0:
        return
    recursive(n-1)  # O(n) - linear recursion
    recursive(n-1)  # O(2ⁿ) - binary recursion
```

### 3. Master Theorem for Divide & Conquer
- T(n) = aT(n/b) + f(n)
- Binary Search: T(n) = T(n/2) + O(1) = O(log n)
- Merge Sort: T(n) = 2T(n/2) + O(n) = O(n log n)

## Common Complexity Requirements

### By Problem Type
| Problem Type | Expected Complexity |
|-------------|-------------------|
| Two Sum (unsorted) | O(n) time |
| Two Sum (sorted) | O(n) time, O(1) space |
| 3Sum | O(n²) time |
| Substring problems | O(n) time |
| Next greater element | O(n) time |
| Top K elements | O(n log k) or O(n) time |

### Space Complexity Constraints
- "Constant space" → O(1) excluding output
- "In-place" → Modify input array
- "No extra space" → O(1) auxiliary space

## My Complexity Analysis Process

1. **Identify loops and their ranges**
2. **Check for nested iterations**
3. **Consider amortized costs**
4. **Account for sorting if present**
5. **Calculate space for data structures**
6. **Consider recursion depth**
7. **Verify against problem constraints**

## Red Flags for Complexity

### Time Complexity Issues
- Nested loops over same array → O(n²)
- Sorting inside loop → O(n² log n)
- Recursive without memoization → Exponential

### Space Complexity Issues
- Recursion depth = input size → O(n) stack space
- Storing all substrings → O(n²) space
- Not cleaning up HashMap → Unbounded space

## Complexity Proof Patterns

### Proving O(n) for Monotonic Stack
"Each element is pushed exactly once and popped at most once. Total operations = 2n = O(n)"

### Proving O(n) for Sliding Window
"Each element enters window once and leaves once. Total operations = 2n = O(n)"

### Proving O(1) Amortized
"Over n operations, total cost is O(n). Average cost per operation = O(n)/n = O(1)"