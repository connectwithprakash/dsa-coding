# Problem-Pattern Mapping

## Quick Reference Table

| Problem | Primary Pattern | Secondary Patterns | Key Technique | Complexity |
|---------|-----------------|-------------------|---------------|------------|
| **Arrays & Hashing** |
| Contains Duplicate | Frequency Counting | Set | HashSet for uniqueness | O(n) / O(n) |
| Valid Anagram | Frequency Counting | - | Character frequency comparison | O(n) / O(1) |
| Two Sum | HashMap | - | Store complements | O(n) / O(n) |
| Group Anagrams | Frequency Counting | HashMap | Frequency signature as key | O(nm) / O(nm) |
| Top K Frequent Elements | Frequency Counting | Bucket Sort | Frequency as bucket index | O(n) / O(n) |
| Product of Array Except Self | Prefix/Suffix | - | Two-pass prefix-suffix products | O(n) / O(1) |
| Valid Sudoku | HashMap | - | Three constraint validation | O(1) / O(1) |
| Encode/Decode Strings | Design | - | Length-prefixed encoding | O(n) / O(1) |
| Longest Consecutive Sequence | HashMap | Set | Identify sequence starts | O(n) / O(n) |
| **Two Pointers** |
| Valid Palindrome | Two Pointers | - | Converging pointers | O(n) / O(1) |
| Two Sum II | Two Pointers | - | Sorted array traversal | O(n) / O(1) |
| 3Sum | Two Pointers | Sorting | Fix one, two-pointer for rest | O(n²) / O(1) |
| Container With Most Water | Two Pointers | Greedy | Move shorter height pointer | O(n) / O(1) |
| Trapping Rain Water | Two Pointers | Prefix/Suffix | Track max from both sides | O(n) / O(1) |
| **Sliding Window** |
| Best Time to Buy and Sell Stock | Sliding Window | Greedy | Track minimum price | O(n) / O(1) |
| Longest Substring Without Repeating | Sliding Window | Set | Variable window with set | O(n) / O(min(n,m)) |
| Longest Repeating Character Replacement | Sliding Window | Frequency Counting | Check (length - max_freq) ≤ k | O(n) / O(1) |
| Permutation in String | Sliding Window | Frequency Counting | Fixed window frequency match | O(n) / O(1) |
| Minimum Window Substring | Sliding Window | Frequency Counting | Variable window with counters | O(n) / O(k) |
| Sliding Window Maximum | Deque/Heap | - | Lazy cleanup or deque | O(n) / O(k) |
| **Stack** |
| Valid Parentheses | Stack | HashMap | Match brackets | O(n) / O(n) |
| Min Stack | Stack | Design | Store (value, min) tuples | O(1) / O(n) |
| Evaluate RPN | Stack | - | Operand stack | O(n) / O(n) |
| Generate Parentheses | Backtracking | DFS | Tree traversal with pruning | O(4^n/√n) / O(n) |
| Daily Temperatures | Monotonic Stack | - | Decreasing stack | O(n) / O(n) |
| Car Fleet | Stack/Sorting | - | Sort by position, check time | O(nlogn) / O(n) |
| Largest Rectangle in Histogram | Monotonic Stack | - | Index inheritance | O(n) / O(n) |

## Pattern Frequency Analysis

### Most Common Primary Patterns
1. **Frequency Counting** - 7 problems
2. **Sliding Window** - 6 problems  
3. **Two Pointers** - 5 problems
4. **Stack** - 4 problems
5. **Monotonic Stack** - 3 problems
6. **Prefix/Suffix** - 2 problems

### Most Common Combinations
1. **Sliding Window + Frequency Counting** - 4 problems
2. **Two Pointers + Greedy** - 2 problems
3. **Stack + Design** - 2 problems

## Pattern Selection by Problem Type

### String Problems
- **Anagrams/Permutations** → Frequency Counting
- **Substrings** → Sliding Window
- **Palindromes** → Two Pointers
- **Parentheses** → Stack

### Array Problems
- **Pairs/Triplets** → Two Pointers (if sorted) or HashMap
- **Subarrays** → Sliding Window or Prefix Sum
- **Next Element** → Monotonic Stack
- **Top K** → Heap or Bucket Sort

### Optimization Problems
- **Maximum/Minimum** → Greedy, DP, or Sliding Window
- **Area/Container** → Two Pointers or Stack
- **Range Queries** → Prefix/Suffix

## Complexity Patterns

### O(n) Solutions
- Single pass with HashMap
- Sliding Window
- Monotonic Stack
- Two Pointers on sorted array

### O(n log n) Solutions
- Sorting + Two Pointers
- Heap operations
- Car Fleet (sorting required)

### O(n²) Solutions
- 3Sum (nested two pointers)
- Brute force that can't be optimized further

## Key Insights by Pattern

### When Multiple Patterns Apply
Some problems can be solved with different patterns:
- **Trapping Rain Water**: Two Pointers OR Prefix/Suffix OR Stack
- **Best Time to Buy Sell**: Sliding Window OR Simple scan with min tracking

### Pattern Evolution
How patterns build on each other:
1. **Two Sum** → **Two Sum II** → **3Sum**
   - HashMap → Two Pointers → Fixed + Two Pointers
   
2. **Valid Parentheses** → **Min Stack** → **Largest Rectangle**
   - Basic Stack → Stack with data → Monotonic Stack

3. **Contains Duplicate** → **Valid Anagram** → **Group Anagrams**
   - Set → Frequency → Frequency as key