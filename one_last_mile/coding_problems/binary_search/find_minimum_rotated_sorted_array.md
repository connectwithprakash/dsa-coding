# Find Minimum in Rotated Sorted Array

## Problem
Suppose an array of length `n` sorted in ascending order is rotated between `1` and `n` times. For example, the array `nums = [0,1,2,4,5,6,7]` might become:
- `[4,5,6,7,0,1,2]` if it was rotated 4 times
- `[0,1,2,4,5,6,7]` if it was rotated 7 times

Given the sorted rotated array `nums` of unique elements, return the minimum element of this array.

You must write an algorithm that runs in `O(log n)` time.

## My Approach

My key insight was that in a rotated sorted array, we need to identify which half contains the rotation point (where the minimum exists). I compare the middle element with the right element:
- If `nums[right] > nums[mid]`: The right half is properly sorted, so minimum must be in left half (including mid)
- If `nums[right] < nums[mid]`: The rotation point is in the right half, so minimum is there

The reason I compare with right instead of left is that the right pointer gives us definitive information about where the break point is.

## Solution

```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Handle single element
        if len(nums) == 1:
            return nums[0]
        
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            if nums[right] > nums[mid]:
                # Right half is sorted, minimum is in left half (including mid)
                right = mid
            else:
                # Right half contains the rotation point, minimum is there
                left = mid + 1
        
        return nums[left]
```

## Visual Intuition

Let me trace through my test cases from my rough solution:

```
Example 1: [3, 4, 5, 6, 1, 2]
           L        M     R
nums[R]=2 < nums[M]=5, so left = mid + 1

           L=3    M=4   R=5
nums[R]=2 > nums[M]=1, so right = mid

           L=3   R=4
           M=3
nums[R]=1 > nums[M]=6, so right = mid (but L >= R, exit)
Return nums[3] = 6 (wait, this seems wrong)

Let me retrace:
[3, 4, 5, 6, 1, 2]
 L     M        R
nums[R]=2 < nums[M]=5, so rotation is in right half
left = mid + 1 = 3

[3, 4, 5, 6, 1, 2]
          L  M  R
nums[R]=2 > nums[M]=1, so right half is sorted
right = mid = 4

[3, 4, 5, 6, 1, 2]
          L=R
Return nums[4] = 1 ✓

Example 2: [4, 5, 6, 7]  (No rotation)
           L     M  R
nums[R]=7 > nums[M]=5, so right = mid

           L  M  R
nums[R]=5 > nums[M]=4, so right = mid

           L=R
Return nums[0] = 4 ✓

Example 3: [2, 3, 1]
           L  M  R
nums[R]=1 < nums[M]=3, so left = mid + 1

              L=R
Return nums[2] = 1 ✓

Example 4: [5, 1, 2, 3, 4]
           L     M     R
nums[R]=4 > nums[M]=2, so right = mid

           L  M  R
nums[R]=2 > nums[M]=1, so right = mid

           L=R
Return nums[1] = 1 ✓
```

## Why Compare with Right?

Comparing with the right pointer gives us clear information:
1. If `nums[mid] < nums[right]`: We know for sure the right portion is sorted normally
2. If `nums[mid] > nums[right]`: We know for sure there's a rotation point in the right portion

Comparing with left would be ambiguous because the left portion might be the larger rotated part or the smaller part.

## Complexity Analysis

- **Time Complexity:** O(log n)
  - Binary search dividing the search space in half each iteration
  - Maximum iterations: log₂(n)
  
- **Space Complexity:** O(1)
  - Only using three pointers regardless of input size

## Edge Cases

1. **No rotation** - Array is already sorted: `[1, 2, 3, 4, 5]`
   - Algorithm correctly returns first element
   
2. **Single element** - `[1]`
   - Handled explicitly, returns the only element
   
3. **Two elements** - `[2, 1]` or `[1, 2]`
   - Works correctly with the comparison logic
   
4. **Full rotation** - Rotated n times returns to original: `[1, 2, 3, 4, 5]`
   - Same as no rotation case

## Key Insights

1. **Right comparison is key** - Comparing with right pointer gives definitive information about which half to search

2. **Include mid when going left** - When right half is sorted, minimum might be mid itself, so use `right = mid` not `right = mid - 1`

3. **Exclude mid when going right** - When rotation is in right half, mid can't be minimum (since nums[mid] > nums[right]), so use `left = mid + 1`

4. **Works for sorted arrays too** - The algorithm naturally handles non-rotated arrays as a special case

## Common Pitfalls

1. **Wrong comparison** - Comparing with left instead of right can lead to incorrect decisions
2. **Off-by-one errors** - Important to use `right = mid` vs `left = mid + 1` correctly
3. **Not handling edge cases** - Single element arrays need special handling

## Pattern Recognition

This problem demonstrates:
- **Binary Search on Rotated Array** - Modified binary search for rotated data
- **Comparison Strategy** - Choosing the right element to compare with
- **Search Space Reduction** - Intelligently eliminating half of the array

Similar problems:
- Search in Rotated Sorted Array
- Find Peak Element
- Search in Rotated Sorted Array II (with duplicates)

## What I Learned

The elegance of this solution is in recognizing that comparing with the right pointer gives us unambiguous information about where the minimum lies. Initially, I was thinking about comparing both sides, but realized that just the right comparison is sufficient. The key insight that both halves are increasing functions, with one potentially having a higher range than the other, led me to this clean solution.