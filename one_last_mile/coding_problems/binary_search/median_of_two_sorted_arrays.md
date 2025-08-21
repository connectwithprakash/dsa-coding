# Median of Two Sorted Arrays

## Problem
Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return the median of the two sorted arrays.

The overall run time complexity should be `O(log(m+n))`.

## My Approach

The key insight I had was that finding the median means dividing all elements into two equal halves. Instead of merging the arrays, I can find the right partition point in both arrays such that:
1. The left halves combined have exactly `(m+n)/2` elements
2. Every element in the left halves is less than or equal to every element in the right halves

Since we know how many total elements should be in the left combined half, if we decide to take `mid` elements from nums1, we must take `half - mid` elements from nums2. This dependency lets us binary search on just one array!

The crucial cross-comparison ensures our partition is valid:
- Last element of nums1's left ≤ First element of nums2's right
- Last element of nums2's left ≤ First element of nums1's right

## Solution

```python
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # To run the algorithm O(log(min(m, n)))
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        total = m + n
        half = total // 2

        left, right = 0, m

        while True:
            mid = (left + right) // 2
            
            # Get values at partition boundaries
            l1_val = nums1[mid-1] if mid > 0 else float("-inf")
            r1_val = nums1[mid] if mid < m else float("inf")
            l2_val = nums2[half-mid-1] if (half-mid) > 0 else float("-inf")
            r2_val = nums2[half-mid] if (half-mid) < n else float("inf")
            
            if l1_val > r2_val:
                # Too many elements from nums1, decrease partition
                right = mid - 1
            elif l2_val > r1_val:
                # Too few elements from nums1, increase partition
                left = mid + 1
            else:
                # Found the correct partition
                if total % 2 == 1:
                    # Odd total: median is min of right elements
                    return min(r1_val, r2_val)
                else:
                    # Even total: median is average of max(left) and min(right)
                    return (max(l1_val, l2_val) + min(r1_val, r2_val)) / 2
```

## Visual Intuition

### Example 1: Even Total Length
```
nums1 = [1, 3, 5, 7]
nums2 = [2, 4, 6, 8]
total = 8, half = 4

Goal: Find partition where we take total 4 elements from left halves

Iteration 1: mid = 2
nums1: [1, 3 | 5, 7]  (take 2 from left)
nums2: [2, 4 | 6, 8]  (take 2 from left)

Check: 3 ≤ 6 ✓ and 4 ≤ 5 ✓
Valid partition found!

Median = (max(3,4) + min(5,6)) / 2 = (4 + 5) / 2 = 4.5
```

### Example 2: Odd Total Length
```
nums1 = [1, 3]
nums2 = [2]
total = 3, half = 1

Iteration 1: mid = 1
nums1: [1 | 3]      (take 1 from left)
nums2: [ | 2]       (take 0 from left)

Check: 1 ≤ 2 ✓ and -∞ ≤ 3 ✓
Valid partition found!

Median = min(3, 2) = 2
```

### Example 3: Binary Search Process
```
nums1 = [1, 2, 3, 4, 5]
nums2 = [6, 7, 8, 9, 10, 11, 12]
total = 12, half = 6

Iteration 1: mid = 2
nums1: [1, 2 | 3, 4, 5]
nums2: [6, 7, 8, 9 | 10, 11, 12]
Check: 2 ≤ 10 ✓ but 9 > 3 ✗
Too few from nums1, left = 3

Iteration 2: mid = 4
nums1: [1, 2, 3, 4 | 5]
nums2: [6, 7 | 8, 9, 10, 11, 12]
Check: 4 ≤ 8 ✓ and 7 ≤ 5 ✗
Too many from nums1, right = 3

Iteration 3: mid = 3
nums1: [1, 2, 3 | 4, 5]
nums2: [6, 7, 8 | 9, 10, 11, 12]
Check: 3 ≤ 9 ✓ and 8 ≤ 4 ✗
Still too few, left = 4

(Continue until convergence...)
```

## Why This Works

The partition approach works because:

1. **Conservation of elements**: If we take `i` elements from nums1's left, we must take exactly `half - i` from nums2's left to maintain the total count.

2. **Cross-comparison validity**: When `l1 ≤ r2` and `l2 ≤ r1`, we guarantee:
   - All elements in combined left ≤ All elements in combined right
   - This is exactly what the median partition requires!

3. **Binary search convergence**: Moving the partition in nums1 automatically adjusts the partition in nums2 in the opposite direction, maintaining the total count.

## Edge Cases

```python
# Edge Case 1: One empty array
nums1 = []
nums2 = [1, 2, 3]
# Partition nums1 at 0, nums2 at 1 or 2

# Edge Case 2: No overlap in values
nums1 = [1, 2]
nums2 = [100, 200]
# Partition puts all of nums1 in left half

# Edge Case 3: Single element arrays
nums1 = [1]
nums2 = [2]
# Median = (1 + 2) / 2 = 1.5

# Edge Case 4: Duplicate values
nums1 = [1, 1]
nums2 = [1, 1]
# Works correctly, median = 1
```

## Complexity Analysis

- **Time Complexity:** O(log(min(m, n)))
  - Binary search on the smaller array
  - Each iteration does O(1) comparisons
  - Maximum iterations: log₂(min(m, n))

- **Space Complexity:** O(1)
  - Only using variables for partition indices and boundary values

## Key Insights

1. **Binary search for partition, not value** - We're not searching for a specific number but for the correct way to split the arrays

2. **Infinity trick for boundaries** - Using ±infinity for out-of-bounds eliminates special cases

3. **Smaller array optimization** - Always binary search on the smaller array for better complexity

4. **Single partition determines both** - Once we choose partition for nums1, nums2's partition is determined

## Pattern Recognition

This problem showcases:
- **Binary Search on Solution Space** - Not searching in array but in partition positions
- **Mathematical Invariant** - Maintaining exactly half elements in combined left
- **Cross-validation** - Checking conditions across different arrays

## What I Learned

The elegance of this solution is recognizing that the median divides elements into two equal halves, and we can find this division without actually merging the arrays. The binary search here isn't looking for a value but for a partition configuration. The cross-comparison (checking if max of left1 ≤ min of right2 and vice versa) ensures our partition respects the sorted order across both arrays. This transforms an O(m+n) merging problem into an O(log(min(m,n))) search problem!