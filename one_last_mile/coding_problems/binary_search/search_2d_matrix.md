# Search a 2D Matrix

## Problem
You are given an `m x n` integer matrix `matrix` with the following two properties:
- Each row is sorted in non-decreasing order.
- The first integer of each row is greater than the last integer of the previous row.

Given an integer `target`, return `true` if `target` is in `matrix` or `false` otherwise.

You must write a solution in `O(log(m * n))` time complexity.

## My Approach

The key insight I had was that this matrix is essentially a sorted 1D array that's been reshaped into 2D. Since each row's first element is greater than the previous row's last element, I can treat it as a flattened sorted array and apply binary search.

The mapping between 1D and 2D indices:
- 1D to 2D: `row = idx // ncols`, `col = idx % ncols`
- 2D to 1D: `idx = row * ncols + col`

## Solution

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nrows = len(matrix)
        ncols = len(matrix[0])
        
        left_idx, right_idx = 0, (nrows * ncols) - 1
        
        while left_idx <= right_idx:
            mid_idx = (left_idx + right_idx) // 2
            # Convert 1D index to 2D coordinates
            row = mid_idx // ncols
            col = mid_idx % ncols
            
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                right_idx = mid_idx - 1
            else:
                left_idx = mid_idx + 1
        
        return False
```

## Visual Intuition

```
Matrix:
[1,  3,  5,  7]
[10, 11, 16, 20]
[23, 30, 34, 60]

Conceptual 1D view:
[1, 3, 5, 7, 10, 11, 16, 20, 23, 30, 34, 60]
 0  1  2  3   4   5   6   7   8   9  10  11  (indices)

Search for target = 11:

Step 1: left=0, right=11, mid=5
        mid_idx=5 → row=5//4=1, col=5%4=1
        matrix[1][1] = 11 ✓ Found!

Search for target = 13:

Step 1: left=0, right=11, mid=5
        mid_idx=5 → row=1, col=1
        matrix[1][1] = 11 < 13, search right
        
Step 2: left=6, right=11, mid=8
        mid_idx=8 → row=2, col=0
        matrix[2][0] = 23 > 13, search left
        
Step 3: left=6, right=7, mid=6
        mid_idx=6 → row=1, col=2
        matrix[1][2] = 16 > 13, search left
        
Step 4: left=6, right=5
        left > right, return False
```

## Index Mapping Examples

For a 3×4 matrix:
```
1D index → 2D coordinates:
0  → (0,0)    4  → (1,0)    8  → (2,0)
1  → (0,1)    5  → (1,1)    9  → (2,1)
2  → (0,2)    6  → (1,2)    10 → (2,2)
3  → (0,3)    7  → (1,3)    11 → (2,3)

Formula verification:
idx=7: row = 7//4 = 1, col = 7%4 = 3 → matrix[1][3] ✓
idx=10: row = 10//4 = 2, col = 10%4 = 2 → matrix[2][2] ✓
```

## Complexity Analysis

- **Time Complexity:** O(log(m × n)) where m is rows and n is columns
  - We perform binary search on m × n elements
  - Each iteration halves the search space
  
- **Space Complexity:** O(1)
  - Only using a few variables regardless of matrix size
  - No recursion, no additional data structures

## Alternative Approaches

### Two Binary Searches
1. Binary search to find the correct row
2. Binary search within that row

```python
def searchMatrix_two_searches(self, matrix: List[List[int]], target: int) -> bool:
    # First binary search: find potential row
    top, bottom = 0, len(matrix) - 1
    while top <= bottom:
        mid_row = (top + bottom) // 2
        if target < matrix[mid_row][0]:
            bottom = mid_row - 1
        elif target > matrix[mid_row][-1]:
            top = mid_row + 1
        else:
            # Target might be in this row
            break
    
    if top > bottom:
        return False
    
    # Second binary search: search within the row
    row = (top + bottom) // 2
    left, right = 0, len(matrix[0]) - 1
    while left <= right:
        mid = (left + right) // 2
        if matrix[row][mid] == target:
            return True
        elif matrix[row][mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    
    return False
```

This approach also achieves O(log m + log n) = O(log(m×n)) but is more complex.

## Key Insights

1. **Virtual flattening** - Treating 2D as 1D without actual memory overhead is a powerful technique

2. **Modulo arithmetic** - The division and modulo operations perfectly map between dimensions:
   - Division (`//`) gives the row (how many complete rows we've passed)
   - Modulo (`%`) gives the column (position within current row)

3. **Matrix properties matter** - This solution only works because the matrix is sorted in a specific way (each row's first element > previous row's last)

## Common Pitfalls

1. **Index calculation errors** - Make sure to use `ncols` not `nrows` for the modulo operation
2. **Empty matrix** - Check for empty matrix or empty rows
3. **Off-by-one** - Remember array indices are 0-based

## Pattern Recognition

This problem combines:
- **Binary Search** - Core algorithm for O(log n) search
- **Matrix traversal** - Understanding 2D to 1D mapping
- **Math patterns** - Using division and modulo for coordinate conversion

## What I Learned

The elegance of treating a 2D sorted matrix as a 1D array shows how mathematical transformations can simplify problems. Instead of dealing with complex 2D boundaries, we reduce it to a standard binary search with simple index arithmetic. This pattern appears in many matrix problems where we need to traverse in a specific order.