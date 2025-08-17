# Pattern Recognition Triggers

## Keyword-to-Pattern Mapping

### Immediate Pattern Indicators

| Keywords/Phrases | Pattern | Why |
|-----------------|---------|-----|
| "next greater element" | Monotonic Stack | Stack maintains candidates waiting for their "next" |
| "next smaller element" | Monotonic Stack | Same principle, different comparison |
| "anagram" | Frequency Counting | Anagrams have identical character frequencies |
| "permutation" (of string) | Frequency Counting | Permutations have same element frequencies |
| "palindrome" | Two Pointers | Check from both ends simultaneously |
| "sorted array" + "find pair" | Two Pointers | Can eliminate candidates systematically |
| "substring" | Sliding Window | Contiguous sequence optimization |
| "subarray" | Sliding Window | Contiguous elements in array |
| "top k frequent" | Heap or Bucket Sort | Need k largest/smallest by some metric |
| "product except self" | Prefix/Suffix | Need info from both directions |

### Constraint-Based Triggers

| Constraint | Pattern | Example |
|-----------|---------|---------|
| "at most k distinct" | Sliding Window | Variable size with frequency tracking |
| "exactly k elements" | Sliding Window | Often = "at most k" - "at most k-1" |
| "consecutive elements" | Sliding Window | Window represents consecutive range |
| "cannot sort array" | HashMap | Need O(n) without sorting |
| "constant space" | Two Pointers | If array is sorted |
| "lowercase letters only" | Array Counting | Use array[26] instead of HashMap |
| "binary values (0/1)" | Two Pointers/Counting | Limited states enable optimization |

### Action-Based Triggers

| Action Description | Pattern | Why |
|-------------------|---------|-----|
| "merge two sorted" | Two Pointers | Process both in single pass |
| "find if exists" | Set/HashMap | O(1) lookup |
| "count occurrences" | Frequency Counting | Track element frequencies |
| "validate matching" | Stack | LIFO for nested structures |
| "find maximum in range" | Monotonic Stack/Deque | Maintain order for efficiency |
| "reverse" | Two Pointers or Stack | Swap from ends or LIFO |
| "remove duplicates" | Set or Two Pointers | Track seen or overwrite in-place |

## Problem Type Recognition

### String Problems

**"Find longest substring with..."**
- Primary: Sliding Window
- Secondary: HashMap for state
- Example: "without repeating characters"

**"Check if s1 is anagram/permutation of s2"**
- Primary: Frequency Counting
- Secondary: Sorting (alternative)
- Example: Valid Anagram

**"Valid parentheses/brackets"**
- Primary: Stack
- Secondary: Counter (if just counting)
- Example: Valid Parentheses

### Array Problems

**"Find pair that sums to target"**
- Sorted: Two Pointers
- Unsorted: HashMap
- Example: Two Sum vs Two Sum II

**"Find triplet/k-elements that..."**
- Primary: Fix elements + Two Pointers
- Secondary: Sorting first
- Example: 3Sum

**"Maximum/minimum in sliding window"**
- Primary: Deque or Heap
- Secondary: Monotonic structure
- Example: Sliding Window Maximum

**"Contiguous subarray with property"**
- Primary: Sliding Window
- Secondary: Prefix Sum
- Example: Maximum subarray sum

### Optimization Problems

**"Container with most water"**
- Primary: Two Pointers
- Secondary: Greedy choice
- Key: Move limiting factor

**"Largest rectangle/area"**
- Primary: Monotonic Stack
- Secondary: Dynamic Programming
- Example: Largest Rectangle in Histogram

**"Buy and sell stock"**
- Single transaction: Track min
- Multiple: Dynamic Programming
- Example: Best Time to Buy and Sell

## Composite Triggers

### Multiple Keywords Present

**"Longest substring" + "at most k"**
- Sliding Window + Frequency Counting
- Example: Longest Repeating Character Replacement

**"Valid" + "parentheses" + "generate"**
- Stack validation + Backtracking generation
- Example: Generate Parentheses

**"Sorted array" + "rotated"**
- Modified Binary Search
- Example: Search in Rotated Sorted Array

## Anti-Patterns (When NOT to Use)

### Don't Use Sliding Window When:
- Elements are non-contiguous
- Need to check all combinations
- Problem requires sorting first

### Don't Use Two Pointers When:
- Array cannot be sorted
- Need to track complex state
- Non-linear traversal required

### Don't Use Monotonic Stack When:
- Don't need "next" relationship
- Simple min/max is sufficient
- Order doesn't matter

## Decision Tree

```
Is input sorted or can be sorted?
├─ YES → Two Pointers or Binary Search
└─ NO → Continue
    │
    Is it about substrings/subarrays?
    ├─ YES → Sliding Window
    └─ NO → Continue
        │
        Need "next greater/smaller"?
        ├─ YES → Monotonic Stack
        └─ NO → Continue
            │
            Counting/frequency involved?
            ├─ YES → HashMap/Frequency Counting
            └─ NO → Continue
                │
                Need info from both directions?
                ├─ YES → Prefix/Suffix
                └─ NO → Check other patterns
```

## My Recognition Process

1. **Read problem twice** - First for understanding, second for keywords
2. **List constraints** - Array size, value ranges, space limits
3. **Identify keywords** - Check against trigger tables
4. **Consider multiple patterns** - Many problems combine 2+ patterns
5. **Start with brute force** - Then optimize with patterns
6. **Verify complexity** - Ensure pattern gives required complexity

## Common Misidentifications

| Looks Like | But Actually | Why Different |
|------------|--------------|---------------|
| Sliding Window | Dynamic Programming | Non-contiguous elements |
| Two Pointers | Binary Search | Need to find exact position |
| Stack | Recursion | No LIFO relationship |
| Frequency Counting | Sorting | Order matters |
| Monotonic Stack | Simple iteration | Don't need "next" element |

## Pattern Combination Triggers

**Frequency + Sliding Window**
- "substring with all characters"
- "window with k distinct"

**Two Pointers + Greedy**
- "optimize area/volume"
- "minimize/maximize with choice"

**Stack + Index Tracking**
- "rectangle problems"
- "span problems"

**Prefix/Suffix + Two Pointers**
- "water trapping"
- "elevation problems"