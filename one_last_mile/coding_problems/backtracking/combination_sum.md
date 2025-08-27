# Combination Sum

## Problem
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

## My Approach

I use backtracking where at each step, I decide whether to:
1. Include the current number again (can reuse)
2. Move to a different number (skip current)

The recursion stops when we've exhausted all options or exceeded the target.

## Solution with Comments (Corrected)

```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combination = []
        combinations = []
        
        def dfs(idx, current_sum):
            # Base cases
            if idx < 0 or current_sum > target:
                return
            
            if current_sum == target:
                combinations.append(combination.copy())
                return
            
            # Choice 1: Include candidates[idx] (can reuse)
            combination.append(candidates[idx])
            dfs(idx, current_sum + candidates[idx])  # Stay at same index
            combination.pop()
            
            # Choice 2: Skip to next candidate
            dfs(idx - 1, current_sum)  # Move to previous index, keep same sum
        
        dfs(len(candidates) - 1, 0)
        return combinations
```

## Standard Forward Approach

```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def backtrack(start_idx, current_combination, remaining_target):
            # Found valid combination
            if remaining_target == 0:
                result.append(current_combination[:])
                return
            
            # Exceeded target, stop exploring
            if remaining_target < 0:
                return
            
            # Try each candidate from start_idx onwards
            for i in range(start_idx, len(candidates)):
                current_combination.append(candidates[i])
                # Key: pass i (not i+1) to allow reuse of same element
                backtrack(i, current_combination, remaining_target - candidates[i])
                current_combination.pop()
        
        backtrack(0, [], target)
        return result
```

## Optimized Solution with Early Pruning

```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()  # Sort for early termination
        result = []
        
        def backtrack(start_idx, path, remaining):
            if remaining == 0:
                result.append(path[:])
                return
            
            for i in range(start_idx, len(candidates)):
                if candidates[i] > remaining:
                    break  # All following elements are too large
                
                path.append(candidates[i])
                backtrack(i, path, remaining - candidates[i])
                path.pop()
        
        backtrack(0, [], target)
        return result
```

## Visual Intuition

### Decision Tree for candidates=[2,3,6,7], target=7

```
                         [] (target=7)
                    /    /    \     \
                  2    3      6      7
                (5)   (4)    (1)    (0) ✓
               / | \   |
             2  3  6   3
            (3)(2)(X) (1)
            /         
           2         
          (1)        
          X

Valid paths:
- [7] → 7
- [2,2,3] → 7
```

### Step-by-Step Execution (Forward Approach)

```
candidates = [2,3,5], target = 8

backtrack(0, [], 8):
├─ Add 2: [2], remaining=6
│  ├─ Add 2: [2,2], remaining=4
│  │  ├─ Add 2: [2,2,2], remaining=2
│  │  │  ├─ Add 2: [2,2,2,2], remaining=0 ✓
│  │  │  └─ Add 3: [2,2,2,3], remaining=-1 ✗
│  │  └─ Add 3: [2,2,3], remaining=1
│  │     └─ Add 5: [2,2,5], remaining=-4 ✗
│  ├─ Add 3: [2,3], remaining=3
│  │  └─ Add 3: [2,3,3], remaining=0 ✓
│  └─ Add 5: [2,5], remaining=1
│     └─ (no valid continuations)
├─ Add 3: [3], remaining=5
│  ├─ Add 3: [3,3], remaining=2
│  │  └─ (no exact match)
│  └─ Add 5: [3,5], remaining=0 ✓
└─ Add 5: [5], remaining=3
   └─ (no exact match)

Result: [[2,2,2,2], [2,3,3], [3,5]]
```

## Why This Works

The algorithm explores all possible combinations by:
1. **Allowing reuse**: Staying at the same index when including an element
2. **Avoiding duplicates**: Only moving forward (or backward in your approach) prevents generating [2,3] and [3,2] separately
3. **Pruning**: Stopping when sum exceeds target

## Complexity Analysis

- **Time Complexity:** O(N^(T/M))
  - N = number of candidates
  - T = target value
  - M = minimal value among candidates
  - Worst case: exponential in the depth of recursion
  
- **Space Complexity:** O(T/M)
  - Maximum recursion depth when using smallest element repeatedly

## Common Patterns and Variations

### 1. Combination Sum II (No Reuse)
```python
def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    candidates.sort()
    result = []
    
    def backtrack(start, path, remaining):
        if remaining == 0:
            result.append(path[:])
            return
        
        for i in range(start, len(candidates)):
            # Skip duplicates
            if i > start and candidates[i] == candidates[i-1]:
                continue
            
            if candidates[i] > remaining:
                break
            
            path.append(candidates[i])
            backtrack(i + 1, path, remaining - candidates[i])  # i+1 for no reuse
            path.pop()
    
    backtrack(0, [], target)
    return result
```

### 2. Combination Sum III (Fixed Length)
```python
def combinationSum3(self, k: int, n: int) -> List[List[int]]:
    result = []
    
    def backtrack(start, path, remaining):
        if len(path) == k and remaining == 0:
            result.append(path[:])
            return
        
        if len(path) >= k or remaining <= 0:
            return
        
        for i in range(start, 10):  # Numbers 1-9
            path.append(i)
            backtrack(i + 1, path, remaining - i)
            path.pop()
    
    backtrack(1, [], n)
    return result
```

## Common Mistakes

1. **Wrong index progression**:
   ```python
   # Wrong: Causes duplicates
   backtrack(0, path, remaining)  # Always starts from 0
   
   # Correct: Start from current position
   backtrack(i, path, remaining)
   ```

2. **Not handling sum properly**:
   ```python
   # Your original bug:
   dfs(idx-1, sum_-nums[idx])  # Wrong sum when excluding
   
   # Correct:
   dfs(idx-1, current_sum)  # Keep same sum when excluding
   ```

3. **Missing base case**:
   ```python
   # Wrong: Infinite recursion
   if current_sum == target:
       result.append(path[:])
       # Missing return!
   
   # Correct:
   if current_sum == target:
       result.append(path[:])
       return
   ```

## Key Insights

1. **Reuse via index control** - Staying at same index allows reuse

2. **Order prevents duplicates** - Forward/backward traversal ensures uniqueness

3. **Sorting enables pruning** - Can break early when element too large

4. **Target tracking options** - Track remaining or current sum

5. **Decision: include vs skip** - Core backtracking choice pattern

## Pattern Recognition

This problem demonstrates:
- **Unbounded knapsack variant** - Can reuse items
- **Target sum pattern** - Finding combinations that sum to target
- **Pruning optimization** - Stop when exceeding target
- **Index-based deduplication** - Prevent duplicate combinations

Similar problems:
- Combination Sum II (each element used once)
- Combination Sum III (exactly k numbers)
- Coin Change (minimum coins needed)
- Target Sum (with +/- operations)

## What I Learned

The solution shows how backtracking handles problems where elements can be reused. The key insight is controlling the index progression - staying at the same index for reuse versus moving forward to avoid it. Your backward approach is unconventional but valid, showing there are multiple ways to traverse the decision space. The pattern of tracking either remaining target or current sum are both valid approaches, with remaining target often leading to cleaner code.