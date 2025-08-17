# Sliding Window Pattern

## What is Sliding Window?
A technique for finding subarrays/substrings that satisfy certain conditions by maintaining a "window" that slides through the data. Instead of recalculating from scratch for each position, we update incrementally.

## When to Use This Pattern

### Problem Characteristics
- Dealing with **contiguous** sequences (subarray/substring)
- Finding optimal (longest/shortest) substring with constraints
- Problems with "at most k" or "exactly k" conditions
- Need to track state within a range

### Keywords That Signal This Pattern
- "substring"
- "subarray" 
- "contiguous"
- "consecutive"
- "window"
- "longest/shortest with condition"
- "at most k"
- "maximum/minimum in sliding window"

## Two Types of Sliding Windows

### 1. Fixed-Size Window
Window size remains constant throughout.

**When to use**:
- Find max/min sum of k consecutive elements
- Check if permutation exists in string
- Find averages of subarrays

**Template**:
```python
def fixed_window(arr, k):
    # Initialize first window
    window_sum = sum(arr[:k])
    result = window_sum
    
    # Slide the window
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i-k]  # Add new, remove old
        result = max(result, window_sum)
    
    return result
```

### 2. Variable-Size Window
Window expands and contracts based on conditions.

**When to use**:
- Find longest substring with condition
- Find shortest substring containing all characters
- Optimize some property

**Template**:
```python
def variable_window(s):
    left = 0
    window_state = {}  # Track state (counts, etc.)
    result = 0
    
    for right in range(len(s)):
        # Expand window by including s[right]
        update_window_add(s[right])
        
        # Contract window while condition is violated
        while window_is_invalid():
            update_window_remove(s[left])
            left += 1
        
        # Update result
        result = max(result, right - left + 1)
    
    return result
```

## Problems I've Solved

### Fixed-Size Windows

#### 1. Permutation in String
**Key insight**: Window size = len(s1), check frequency match
```python
for i in range(len(s1), len(s2)):
    # Add new character
    window_count[s2[i]] += 1
    # Remove old character  
    window_count[s2[i - len(s1)]] -= 1
    # Check if frequencies match
```

#### 2. Sliding Window Maximum (Hybrid approach)
**Key insight**: Used heap with lazy cleanup instead of pure sliding window
```python
# Add to heap, cleanup stale elements when needed
while heap and heap[0][1] <= (idx - k):
    heappop(heap)
```

### Variable-Size Windows

#### 1. Longest Substring Without Repeating Characters
**Key insight**: Expand until duplicate, contract to remove duplicate
```python
while char in seen:
    seen.remove(s[left])
    left += 1
seen.add(char)
max_len = max(max_len, right - left + 1)
```

#### 2. Longest Repeating Character Replacement
**Key insight**: Valid window when `(length - max_freq) <= k`
```python
if (window_len - max_frequency) <= k:
    max_len = max(max_len, window_len)
else:
    # Shrink window
    counter[s[left]] -= 1
    left += 1
```

#### 3. Minimum Window Substring
**Key insight**: Expand to include all chars, contract to find minimum
```python
while contains_all_chars():
    min_window = min(min_window, current_window)
    # Try to shrink
    remove(s[left])
    left += 1
```

## Advanced Techniques

### Two-Condition Windows
Sometimes need to track multiple conditions:
```python
while condition1_violated or condition2_violated:
    # Shrink window
    if condition1_violated:
        # Handle condition 1
    if condition2_violated:
        # Handle condition 2
```

### Window State Management
Common state tracking approaches:

1. **Frequency map**: `counter = defaultdict(int)`
2. **Set for uniqueness**: `seen = set()`
3. **Running sum/product**: `window_sum += new - old`
4. **Min/max in window**: Use deque or heap

### Optimization: Early Termination
```python
if window_size == optimal_possible:
    return result  # Can't do better
```

## Complexity Analysis
- **Fixed window**: O(n) time, O(1) or O(k) space
- **Variable window**: O(n) time for single pass, O(min(n, alphabet_size)) space

## Common Pitfalls

1. **Off-by-one errors** - Window size is `right - left + 1`
2. **Forgetting to update state** - Both when expanding AND contracting
3. **Wrong shrinking condition** - Know when window becomes invalid
4. **Not handling empty windows** - Check `left <= right`

## Evolution from Brute Force

### Brute Force (Check all substrings)
```python
# O(n³) - Generate all substrings and check each
for i in range(n):
    for j in range(i, n):
        substring = s[i:j+1]
        if valid(substring):  # O(n) check
            update_result()
```

### Sliding Window Optimization
```python
# O(n) - Single pass with incremental updates
left = 0
for right in range(n):
    # O(1) incremental update instead of O(n) recomputation
    update_window_state()
    while invalid():
        shrink_window()
```

## Visual Intuition

```
String: "ADOBECODEBANC", Target: "ABC"
Finding minimum window containing all characters:

[A D O B E C] O D E B A N C  -> Contains A,B,C
 ^         ^
left      right

A [D O B E C O D E B A N C]  -> Move left, still valid
   ^                       ^
  left                   right

A D O B E [C O D E B A N C]  -> Found smaller window
           ^             ^
          left         right
```

## Pattern Combinations

### Sliding Window + Frequency Counting
Most common combination:
- Longest Repeating Character Replacement
- Permutation in String
- Minimum Window Substring

### Sliding Window + Two Pointers
When window boundaries move independently:
- Some optimization problems
- Complex constraint satisfaction

## My Key Learnings

1. **Fixed vs Variable is the first decision** - Problem constraints usually make this clear
2. **State management is crucial** - What info must I track in the window?
3. **Shrinking condition must be precise** - This determines correctness
4. **Window size formula**: Always `right - left + 1` for inclusive bounds
5. **Incremental updates** - The whole point is avoiding recomputation
6. **Sometimes "at most k" = "exactly k" - "at least k"** - Useful transformation

## When NOT to Use Sliding Window

- Non-contiguous elements needed
- Need to consider all pairs (not just ranges)
- Problem requires sorting first
- Multiple non-overlapping windows

## Related Patterns
- **Two Pointers** - Similar but pointers can move independently
- **Prefix Sum** - For range sum queries
- **Monotonic Queue/Stack** - For min/max in sliding window