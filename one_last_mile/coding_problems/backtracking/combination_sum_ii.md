# Combination Sum II

## Problem
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

## My Approach

I use frequency counting to handle duplicates elegantly. By tracking how many times each unique value can be used, I ensure no duplicate combinations while allowing multiple uses of the same value (up to its frequency).

## Solution with Comments

```python
from collections import Counter

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combination = []  # Current combination being built
        combinations = []  # All valid combinations found
        
        # Count frequency of each unique value to handle duplicates
        # e.g., [1,1,2,5,6,7,10] → {1:2, 2:1, 5:1, 6:1, 7:1, 10:1}
        freq_count = Counter(candidates)
        
        # Work with unique sorted values for systematic exploration
        candidates = sorted(freq_count.keys())
        
        def dfs(idx, current_sum):
            # Base cases: out of bounds or exceeded target
            if idx < 0 or current_sum > target:
                return
            
            # Found valid combination
            if current_sum == target:
                combinations.append(combination.copy())
                return
            
            # Choice 1: Include candidates[idx] if available
            # Check frequency to ensure we don't use more than available
            if freq_count[candidates[idx]] > 0:
                # Use this element
                combination.append(candidates[idx])
                freq_count[candidates[idx]] -= 1  # Decrease available count
                
                # Stay at same index to potentially use again (if frequency allows)
                dfs(idx, current_sum + candidates[idx])
                
                # Backtrack: restore state
                combination.pop()
                freq_count[candidates[idx]] += 1  # Restore available count
            
            # Choice 2: Skip to next unique candidate
            # Move to different value to explore other combinations
            dfs(idx - 1, current_sum)
        
        # Start from last index (backward traversal)
        dfs(len(candidates) - 1, 0)
        
        return combinations
```

## Standard Forward Approach

```python
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()  # Sort to group duplicates together
        result = []
        
        def backtrack(start, path, remaining):
            # Found valid combination
            if remaining == 0:
                result.append(path[:])
                return
            
            # Exceeded target
            if remaining < 0:
                return
            
            for i in range(start, len(candidates)):
                # Skip duplicates: if same as previous and we're not at start
                # This ensures we only use each duplicate value once per position
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                # Pruning: no point continuing if current element exceeds remaining
                if candidates[i] > remaining:
                    break
                
                path.append(candidates[i])
                # Move to i+1 since each element can only be used once
                backtrack(i + 1, path, remaining - candidates[i])
                path.pop()
        
        backtrack(0, [], target)
        return result
```

## Visual Intuition

### Example: candidates = [10,1,2,7,6,1,5], target = 8

```
After sorting: [1,1,2,5,6,7,10]
With frequency: {1:2, 2:1, 5:1, 6:1, 7:1, 10:1}

Decision tree using frequency approach:
                     [] (sum=0)
                /         |          \
           1(freq=2)   2(freq=1)   5(freq=1)...
            /    \         |           |
       1(freq=1) skip    5,6,7       skip
         /  \
      2,5,6  skip
      
Valid combinations:
[1,1,6] = 8 ✓
[1,2,5] = 8 ✓
[1,7] = 8 ✓
[2,6] = 8 ✓
```

### Why Frequency Counting Works

```
Original: [1,1,2,5,6,7,10]

Without frequency control:
- Could generate [1,2,5] twice (using different 1's)
- Could generate [1,1,6] and [1,1,6] separately

With frequency control:
- Track {1:2, 2:1, 5:1, ...}
- When using 1, decrease count
- Ensures systematic exploration without duplicates
```

## Complexity Analysis

- **Time Complexity:** O(2^n)
  - In worst case, explore all subsets
  - n is the number of unique elements
  
- **Space Complexity:** O(n)
  - Recursion stack depth
  - Frequency counter storage

## Alternative Approach - Using Visited Array

```python
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        used = [False] * n
        result = []
        
        def backtrack(idx, path, remaining):
            if remaining == 0:
                result.append(path[:])
                return
            
            for i in range(idx, n):
                # Skip if used or duplicate of previous unused
                if used[i] or (i > 0 and candidates[i] == candidates[i-1] and not used[i-1]):
                    continue
                
                if candidates[i] > remaining:
                    break
                
                used[i] = True
                path.append(candidates[i])
                backtrack(i + 1, path, remaining - candidates[i])
                path.pop()
                used[i] = False
        
        backtrack(0, [], target)
        return result
```

## Common Mistakes

1. **Not handling duplicates properly**:
   ```python
   # Wrong: Generates duplicate combinations
   for i in range(start, len(candidates)):
       path.append(candidates[i])
       backtrack(i + 1, path, remaining)
   
   # Correct: Skip duplicates
   if i > start and candidates[i] == candidates[i-1]:
       continue
   ```

2. **Frequency tracking errors**:
   ```python
   # Wrong: Forgetting to restore frequency
   freq_count[val] -= 1
   dfs(idx, sum + val)
   # Missing: freq_count[val] += 1
   
   # Correct: Always restore after backtracking
   freq_count[val] -= 1
   dfs(idx, sum + val)
   freq_count[val] += 1
   ```

3. **Wrong index progression**:
   ```python
   # Wrong: Allows reuse (like Combination Sum I)
   dfs(idx, current_sum + candidates[idx])
   
   # Correct for standard approach: Move to next
   backtrack(i + 1, path, remaining)
   ```

## Key Differences from Combination Sum I

| Aspect | Combination Sum I | Combination Sum II |
|--------|------------------|-------------------|
| Element Usage | Unlimited reuse | Use each once |
| Input | Distinct integers | May have duplicates |
| Index Progress | Stay at same index | Move to next index |
| Duplicate Handling | Not needed | Critical requirement |

## Key Insights

1. **Frequency tracking prevents duplicates** - Systematic way to handle repeated values

2. **Sorting groups duplicates** - Makes skip logic simpler in standard approach

3. **"Use once" means once per element** - Not once per value

4. **Backward traversal works** - Your approach is valid alternative to forward

5. **State restoration is crucial** - Frequency must be restored during backtrack

## Pattern Recognition

This problem demonstrates:
- **Controlled element usage** - Frequency-based exploration
- **Duplicate elimination** - Avoiding same combinations
- **Modified backtracking** - Adapting pattern for constraints
- **0/1 knapsack variant** - Each item used at most once

Similar problems:
- Subsets II (handle duplicates in subsets)
- Permutations II (handle duplicates in permutations)
- 3Sum (find unique triplets)
- 4Sum (find unique quadruplets)

## What I Learned

Your frequency counting approach elegantly solves the duplicate combination problem by transforming it into a controlled usage problem. Instead of skipping duplicates during traversal, you track how many times each unique value can be used. This is particularly clever because it separates the "what values to use" from "how many times to use them". The backward traversal with frequency control ensures systematic exploration without generating duplicate combinations. This shows that there are often multiple valid approaches to handling constraints in backtracking problems.