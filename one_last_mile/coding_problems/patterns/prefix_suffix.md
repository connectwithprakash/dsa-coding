# Prefix/Suffix Pattern

## What is Prefix/Suffix Pattern?
A technique that pre-computes cumulative information from the start (prefix) or end (suffix) of an array. This allows O(1) range queries or calculations that would otherwise require O(n) traversal.

## When to Use This Pattern

### Problem Characteristics
- Need cumulative information (sum, product, max, min)
- Range queries without modification
- Problems asking for "product/sum except self"
- Water trapping or elevation problems
- Need information from both directions

### Keywords That Signal This Pattern
- "product of array except self"
- "cumulative"
- "range sum"
- "prefix sum"
- "running total"
- "from both ends"
- "left and right"
- "water trapping"

## Core Concepts

### 1. Basic Prefix Array
```python
def build_prefix(arr):
    n = len(arr)
    prefix = [0] * n
    prefix[0] = arr[0]
    
    for i in range(1, n):
        prefix[i] = prefix[i-1] + arr[i]  # Or any operation
    
    return prefix
```

### 2. Basic Suffix Array
```python
def build_suffix(arr):
    n = len(arr)
    suffix = [0] * n
    suffix[n-1] = arr[n-1]
    
    for i in range(n-2, -1, -1):
        suffix[i] = suffix[i+1] + arr[i]  # Or any operation
    
    return suffix
```

### 3. Combined Prefix-Suffix
```python
def prefix_suffix_combine(arr):
    n = len(arr)
    result = [0] * n
    
    # Build prefix
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= arr[i]
    
    # Build suffix and combine
    suffix = 1
    for i in range(n-1, -1, -1):
        result[i] *= suffix
        suffix *= arr[i]
    
    return result
```

## Problems I've Solved

### 1. Product of Array Except Self
**Pattern**: Prefix and suffix products
**Key insight**: result[i] = prefix[i-1] × suffix[i+1]
```python
def productExceptSelf(nums):
    n = len(nums)
    result = [1] * n
    
    # Prefix products
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]
    
    # Suffix products (multiply into result)
    suffix = 1
    for i in range(n-1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]
    
    return result
```

### 2. Trapping Rain Water (One Solution)
**Pattern**: Prefix max and suffix max
**Key insight**: Water at position = min(left_max, right_max) - height
```python
def trap(height):
    n = len(height)
    if n < 3:
        return 0
    
    # Prefix max (max height to the left)
    left_max = [0] * n
    left_max[0] = height[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], height[i])
    
    # Suffix max (max height to the right)
    right_max = [0] * n
    right_max[n-1] = height[n-1]
    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], height[i])
    
    # Calculate water
    water = 0
    for i in range(n):
        water += min(left_max[i], right_max[i]) - height[i]
    
    return water
```

## Advanced Techniques

### Space-Optimized Prefix/Suffix
Instead of arrays, use variables when possible:
```python
def optimized_product_except_self(nums):
    n = len(nums)
    result = [1] * n
    
    # Single pass with two pointers
    left = 1
    right = 1
    for i in range(n):
        result[i] *= left
        result[n-1-i] *= right
        left *= nums[i]
        right *= nums[n-1-i]
    
    return result
```

### Range Query with Prefix Sum
```python
class RangeSum:
    def __init__(self, nums):
        self.prefix = [0]
        for num in nums:
            self.prefix.append(self.prefix[-1] + num)
    
    def query(self, left, right):
        # Sum from index left to right (inclusive)
        return self.prefix[right + 1] - self.prefix[left]
```

### 2D Prefix Sum
For matrix range sum queries:
```python
def build_2d_prefix(matrix):
    m, n = len(matrix), len(matrix[0])
    prefix = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            prefix[i][j] = matrix[i-1][j-1] + \
                          prefix[i-1][j] + \
                          prefix[i][j-1] - \
                          prefix[i-1][j-1]
    
    return prefix
```

## Complexity Analysis
- **Time**: O(n) for building prefix/suffix arrays
- **Space**: O(n) for arrays, can be O(1) with optimization
- **Query**: O(1) for range queries after preprocessing

## Common Patterns & Variations

### 1. Prefix Product
```python
prefix_prod[i] = prefix_prod[i-1] * arr[i]
```

### 2. Prefix Maximum/Minimum
```python
prefix_max[i] = max(prefix_max[i-1], arr[i])
```

### 3. Prefix XOR
```python
prefix_xor[i] = prefix_xor[i-1] ^ arr[i]
```

### 4. Difference Array (Inverse of Prefix)
```python
# For range updates
diff[start] += val
diff[end + 1] -= val
# Apply: prefix sum of diff array
```

## Visual Intuition

```
Array: [1, 2, 3, 4]
Product Except Self:

Prefix products:  [1, 1, 2, 6]    (products before each index)
Suffix products:  [24, 12, 4, 1]  (products after each index)
Result:          [24, 12, 8, 6]   (prefix × suffix)

Water Trapping:
Heights:    [0,1,0,2,1,0,1,3,2,1,2,1]
Left max:   [0,1,1,2,2,2,2,3,3,3,3,3]
Right max:  [3,3,3,3,3,3,3,3,2,2,2,1]
Water:      [0,0,1,0,1,2,1,0,0,1,0,0]
```

## Common Pitfalls

1. **Off-by-one errors** - Careful with array boundaries
2. **Not handling empty arrays** - Check edge cases
3. **Integer overflow** - Consider using long for products
4. **Modifying input array** - Sometimes not allowed

## Optimization Strategies

### 1. Single Pass When Possible
```python
# Two-pointer approach for symmetric operations
for i in range(n):
    # Process from left
    # Process from right using n-1-i
```

### 2. Reuse Arrays
```python
# Use result array as temporary storage
result = [1] * n
# Use result to store prefix
# Then modify in-place with suffix
```

### 3. Lazy Evaluation
Only compute prefix/suffix values when needed:
```python
def get_prefix(i):
    if i in cache:
        return cache[i]
    # Compute and cache
```

## My Key Learnings

1. **Two passes are often enough** - Forward for prefix, backward for suffix
2. **Space-time tradeoff** - Arrays for O(1) queries vs variables for O(1) space
3. **Combining operations** - Can often merge prefix and suffix in result array
4. **Range queries become O(1)** - Powerful for repeated queries
5. **Works for any associative operation** - Sum, product, XOR, min, max

## Related Patterns
- **Dynamic Programming** - Prefix sum is a simple DP
- **Two Pointers** - Can sometimes replace prefix/suffix arrays
- **Segment Trees** - For range queries with updates
- **Binary Indexed Trees** - Alternative for prefix sums with updates

## When NOT to Use Prefix/Suffix
- When array is frequently modified
- When only need single query (not worth preprocessing)
- When operation is not associative
- When space is extremely limited