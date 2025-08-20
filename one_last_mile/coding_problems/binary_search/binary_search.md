# Binary Search

## Problem
Given an array of integers `nums` which is sorted in ascending order, and an integer `target`, write a function to search `target` in `nums`. If `target` exists, then return its index. Otherwise, return `-1`.

You must write an algorithm with `O(log n)` runtime complexity.

## My Approach

Initially, I tried a recursive approach with some extra boundary checks that seemed logical but actually caused bugs. The key insight I learned is that binary search should be simple - we don't need complex boundary conditions beyond checking if our search range is valid.

### Initial Buggy Solution
```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(left_idx, right_idx):
            if (left_idx == right_idx):
                return left_idx if target == nums[left_idx] else -1
            mid = (right_idx + left_idx) // 2
            if nums[mid] == target:
                return mid
            # BUG: These conditions prevent valid searches!
            if (mid > left_idx) and (nums[mid] > target):
                return binary_search(left_idx, mid-1)
            elif (mid < right_idx) and (nums[mid] < target):
                return binary_search(mid+1, right_idx)
            else:
                return -1

        return binary_search(0, len(nums)-1)
```

**What went wrong:** The conditions `(mid > left_idx)` and `(mid < right_idx)` were unnecessary and harmful. They prevented searching when `mid` equaled the boundaries, causing the algorithm to incorrectly return -1 for valid targets at the edges of the search range.

## Corrected Solutions

### Recursive Approach
```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(left_idx, right_idx):
            # Base case: empty range
            if left_idx > right_idx:
                return -1
            
            # Calculate middle index
            mid = (left_idx + right_idx) // 2
            
            # Found the target
            if nums[mid] == target:
                return mid
            
            # Target is in left half
            if nums[mid] > target:
                return binary_search(left_idx, mid - 1)
            
            # Target is in right half
            else:  # nums[mid] < target
                return binary_search(mid + 1, right_idx)
        
        return binary_search(0, len(nums) - 1)
```

### Iterative Approach (Preferred)
```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1  # Search left half
            else:
                left = mid + 1   # Search right half
        
        return -1
```

## Visual Intuition

```
Search for target = 7 in [1, 3, 5, 7, 9, 11, 13]

Initial:  [1, 3, 5, 7, 9, 11, 13]
          L        M           R
          mid = 7, found!

Search for target = 5 in [1, 3, 5, 7, 9, 11, 13]

Step 1:   [1, 3, 5, 7, 9, 11, 13]
          L        M           R
          mid = 7 > 5, search left

Step 2:   [1, 3, 5]
          L   M   R
          mid = 3 < 5, search right

Step 3:   [5]
          L/M/R
          mid = 5, found!

Search for target = 4 in [1, 3, 5, 7, 9]

Step 1:   [1, 3, 5, 7, 9]
          L     M     R
          mid = 5 > 4, search left

Step 2:   [1, 3]
          L   R
          M
          mid = 1 < 4, search right

Step 3:   [3]
          L/M/R
          mid = 3 < 4, search right

Step 4:   []  (left > right)
          Return -1
```

## Complexity Analysis

### Recursive Approach
- **Time Complexity:** O(log n) - We halve the search space in each recursive call
- **Space Complexity:** O(log n) - Recursion stack depth equals the number of halvings

### Iterative Approach  
- **Time Complexity:** O(log n) - We halve the search space in each iteration
- **Space Complexity:** O(1) - Only using a few variables

The iterative approach is generally preferred because it uses constant space and avoids potential stack overflow for very large arrays.

## Key Insights

1. **Simplicity is key** - Binary search doesn't need complex boundary checks. The core logic is: check middle, go left if target is smaller, go right if larger.

2. **Watch the loop condition** - Use `left <= right` not `left < right`. The equal case is important for single-element ranges.

3. **Integer overflow consideration** - In some languages, `(left + right) / 2` can overflow. The safe formula is `left + (right - left) / 2`. Python handles big integers automatically.

4. **Edge cases to consider:**
   - Empty array
   - Single element array
   - Target at boundaries (first or last element)
   - Target not in array

## Common Variations

1. **Find first/last occurrence** - When duplicates exist
2. **Find insertion position** - Where to insert target to maintain order
3. **Search in rotated array** - Array is sorted but rotated
4. **Search in 2D matrix** - Treating 2D array as 1D sorted array

## Pattern Recognition

This is the classic binary search pattern. Look for:
- Sorted array or monotonic property
- Need for O(log n) search
- Finding exact match or insertion point
- Problems that can be transformed into sorted search

## What I Learned

My initial solution tried to be "too smart" with extra conditions that actually broke the algorithm. Binary search is elegant in its simplicity - trust the basic logic of halving the search space. The bug taught me that unnecessary complexity often introduces errors rather than preventing them.