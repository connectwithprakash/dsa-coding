# Permutations

## Problem Statement
Given an array of distinct integers, return all possible permutations.

## My Approach

Initially tried to apply the combination sum pattern with backtracking, but realized permutations require a fundamentally different approach. The key insight came from visualizing the tree structure - each number can be inserted at all possible positions in previously formed permutations.

### Visual Intuition

Starting with [1,2,3], the building process looks like:
```
Start: []
Add 1: [1]
Add 2: [2,1], [1,2]  (insert 2 at position 0 and 1)
Add 3: [3,2,1], [2,3,1], [2,1,3],  (from [2,1])
       [3,1,2], [1,3,2], [1,2,3]   (from [1,2])
```

Each level expands by inserting the new element at every valid position in existing permutations.

## Solutions

### Solution 1: Recursive Approach

```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Base case: empty list has one permutation - the empty permutation
        if len(nums) == 0:
            return [[]]

        # Recursive step: Get all permutations of nums[1:]
        # This gives us smaller permutations to build upon
        permutations = self.permute(nums[1:])
        
        result = []
        # For each existing permutation from the recursive call
        for permutation in permutations:
            # Insert nums[0] at every possible position
            # A permutation of length n has n+1 insertion positions:
            # before index 0, before index 1, ..., after index n-1
            for idx in range(len(permutation)+1):
                # Create a new permutation by copying the existing one
                new_permutation = permutation.copy()
                # Insert current element at position idx
                new_permutation.insert(idx, nums[0])
                result.append(new_permutation)

        return result
```

**Time Complexity:** $$O(n! \times n^2)$$
- We generate n! permutations
- For each permutation, we do O(n) insertions
- Each insertion with copy takes O(n) time

**Space Complexity:** $$O(n! \times n)$$
- Store n! permutations, each of length n

### Solution 2: Iterative Approach

```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Start with the empty permutation
        permutations = [[]]
        
        # Process each number one by one
        for num in nums:
            new_permutations = []
            # For each existing permutation
            for permutation in permutations:
                # Insert current number at all possible positions
                # If permutation has k elements, there are k+1 positions
                for idx in range(len(permutation)+1):
                    # Create new permutation with num inserted at position idx
                    new_permutation = permutation.copy()
                    new_permutation.insert(idx, num)
                    new_permutations.append(new_permutation)
            # Replace old permutations with newly generated ones
            # This grows the permutation size by 1 each iteration
            permutations = new_permutations
                    
        return permutations
```

**Time Complexity:** $$O(n! \times n^2)$$ - Same as recursive
**Space Complexity:** $$O(n! \times n)$$ - Same as recursive

## Key Insights

1. **Position-based generation**: Unlike combinations where we choose elements, permutations require placing each element at all possible positions.

2. **Growth pattern**: At each step with k existing permutations of length m, adding a new element creates k × (m+1) new permutations.

3. **No backtracking needed**: The insert-at-all-positions approach naturally avoids duplicates without needing to track visited elements.

## What I Learned

The permutations problem taught me that not all recursive problems require traditional backtracking. The "insert at all positions" pattern is particularly powerful for ordering problems. The recursive solution builds from the bottom up (starting with the last element), while the iterative solution builds from the top down (starting with the first element). Both achieve the same result through different traversal orders.

## Common Pitfalls

1. **Trying to use combination patterns**: Permutations care about order, not just selection
2. **Forgetting to copy**: Must create new lists to avoid modifying existing permutations
3. **Off-by-one errors**: Remember that a list of length n has n+1 insertion positions

## Related Problems
- Permutations II (with duplicates)
- Next Permutation
- Combination Sum (different pattern but often confused)