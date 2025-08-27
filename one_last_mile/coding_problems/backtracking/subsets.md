# Subsets

## Problem
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

## My Approach

I use backtracking with a decision tree approach. For each element, I make two choices: include it in the current subset or exclude it. This naturally generates all 2^n possible subsets.

## Solution with Comments

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []  # Store all subsets
        subset = []   # Current subset being built
        
        def dfs(idx):
            # Base case: processed all elements
            if idx >= len(nums):
                subsets.append(subset.copy())  # Important: copy the current subset
                return
            
            # Choice 1: Include nums[idx] in subset
            subset.append(nums[idx])
            dfs(idx + 1)  # Explore with this element included
            
            # Backtrack: Remove the element
            subset.pop()
            
            # Choice 2: Exclude nums[idx] from subset
            dfs(idx + 1)  # Explore without this element
        
        dfs(0)  # Start from index 0
        return subsets
```

## Alternative Solution - Iterative Approach

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]  # Start with empty subset
        
        for num in nums:
            # For each number, add it to all existing subsets
            new_subsets = []
            for subset in subsets:
                new_subsets.append(subset + [num])
            subsets.extend(new_subsets)
        
        return subsets
```

## Alternative Solution - Using Binary Representation

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        subsets = []
        
        # Generate all 2^n binary numbers
        for mask in range(2**n):
            subset = []
            for i in range(n):
                # Check if i-th bit is set
                if mask & (1 << i):
                    subset.append(nums[i])
            subsets.append(subset)
        
        return subsets
```

## Visual Intuition

### Decision Tree for [1,2,3]

```
                        []
                    /        \
            Include 1         Exclude 1
                [1]              []
              /     \          /     \
        Inc 2      Exc 2   Inc 2    Exc 2
         [1,2]      [1]      [2]      []
        /    \     /   \    /   \    /   \
    Inc3  Exc3 Inc3 Exc3 Inc3 Exc3 Inc3 Exc3
   [1,2,3][1,2][1,3] [1] [2,3] [2]  [3]  []
```

### Step-by-Step Execution

```
nums = [1,2,3]

dfs(0): subset = []
  ├─ Add 1: subset = [1]
  │  └─ dfs(1): subset = [1]
  │     ├─ Add 2: subset = [1,2]
  │     │  └─ dfs(2): subset = [1,2]
  │     │     ├─ Add 3: subset = [1,2,3]
  │     │     │  └─ dfs(3): Add [1,2,3] ✓
  │     │     └─ Pop 3: subset = [1,2]
  │     │        └─ dfs(3): Add [1,2] ✓
  │     └─ Pop 2: subset = [1]
  │        └─ dfs(2): subset = [1]
  │           ├─ Add 3: subset = [1,3]
  │           │  └─ dfs(3): Add [1,3] ✓
  │           └─ Pop 3: subset = [1]
  │              └─ dfs(3): Add [1] ✓
  └─ Pop 1: subset = []
     └─ dfs(1): subset = []
        ├─ Add 2: subset = [2]
        │  └─ dfs(2): subset = [2]
        │     ├─ Add 3: subset = [2,3]
        │     │  └─ dfs(3): Add [2,3] ✓
        │     └─ Pop 3: subset = [2]
        │        └─ dfs(3): Add [2] ✓
        └─ Pop 2: subset = []
           └─ dfs(2): subset = []
              ├─ Add 3: subset = [3]
              │  └─ dfs(3): Add [3] ✓
              └─ Pop 3: subset = []
                 └─ dfs(3): Add [] ✓

Result: [[], [1], [1,2], [1,2,3], [1,3], [2], [2,3], [3]]
```

## Why This Works

The algorithm explores a binary decision tree where at each level we decide whether to include the current element. This guarantees we generate all possible combinations:
- Each element has 2 choices (include/exclude)
- n elements → 2^n total subsets
- The backtracking ensures we explore both choices systematically

## Complexity Analysis

- **Time Complexity:** O(n × 2^n)
  - 2^n subsets to generate
  - Each subset takes O(n) to copy
  
- **Space Complexity:** O(n)
  - Recursion depth is O(n)
  - Not counting output space

## Pattern Variations

### 1. Subsets with Duplicates
```python
def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
    nums.sort()  # Sort to group duplicates
    subsets = []
    subset = []
    
    def dfs(idx):
        if idx == len(nums):
            subsets.append(subset[:])
            return
        
        # Include nums[idx]
        subset.append(nums[idx])
        dfs(idx + 1)
        subset.pop()
        
        # Skip duplicates when excluding
        while idx + 1 < len(nums) and nums[idx] == nums[idx + 1]:
            idx += 1
        dfs(idx + 1)
    
    dfs(0)
    return subsets
```

### 2. Subsets of Size K
```python
def combine(self, n: int, k: int) -> List[List[int]]:
    result = []
    
    def dfs(start, path):
        if len(path) == k:
            result.append(path[:])
            return
        
        for i in range(start, n + 1):
            path.append(i)
            dfs(i + 1, path)
            path.pop()
    
    dfs(1, [])
    return result
```

## Common Mistakes

1. **Forgetting to copy the subset**:
   ```python
   # Wrong: Appends reference, all will be empty at end
   subsets.append(subset)
   
   # Correct: Append a copy
   subsets.append(subset.copy())
   ```

2. **Not handling both choices**:
   ```python
   # Wrong: Only explores one branch
   subset.append(nums[idx])
   dfs(idx + 1)
   
   # Correct: Explore both include and exclude
   subset.append(nums[idx])
   dfs(idx + 1)
   subset.pop()
   dfs(idx + 1)
   ```

3. **Wrong base case**:
   ```python
   # Wrong: Misses the last subset
   if idx > len(nums):
       return
   
   # Correct: Check when equals length
   if idx >= len(nums):
       subsets.append(subset.copy())
   ```

## Key Insights

1. **Binary choice pattern** - Each element is either in or out

2. **Order doesn't matter** - [1,2] and [2,1] are the same subset

3. **Include before exclude** - Convention, but either order works

4. **Copy is crucial** - Python lists are mutable references

5. **2^n is inevitable** - Can't optimize the fundamental complexity

## Pattern Recognition

This problem demonstrates:
- **Classic backtracking** - Choose, explore, unchoose
- **Decision tree traversal** - Binary choices at each level
- **Power set generation** - All possible combinations
- **State space exploration** - Systematic enumeration

Similar problems:
- Combinations
- Permutations
- Letter Combinations of a Phone Number
- Generate Parentheses

## What I Learned

The solution perfectly demonstrates the backtracking pattern with its choose-explore-unchoose structure. The key insight is that generating all subsets is equivalent to making a binary decision for each element. The pattern of including an element, recursing, then backtracking and excluding it ensures we explore the entire decision tree. This foundational pattern extends to many combinatorial problems where we need to generate all possible selections.