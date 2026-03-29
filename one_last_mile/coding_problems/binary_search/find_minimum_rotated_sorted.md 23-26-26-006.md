# Find Minimum in Rotated Sorted Array

## Problem
Suppose an array of length `n` sorted in ascending order is rotated between `1` and `n` times. For example, the array `nums = [0,1,2,4,5,6,7]` might become:
- `[4,5,6,7,0,1,2]` if it was rotated 4 times
- `[0,1,2,4,5,6,7]` if it was rotated 7 times

Given the sorted rotated array `nums` of unique elements, return the minimum element of this array.

You must write an algorithm that runs in `O(log n)` time.

## My Approach

The key insight I had was that in a rotated sorted array, we have two sorted portions, and the minimum element is at the rotation point. By comparing the middle element with the right element, I can determine which half contains the rotation point.

Why compare with right instead of left? The right comparison gives us definitive information:
- If `nums[mid] < nums[right]`: The right portion is properly sorted, so the minimum must be in the left half (including mid)
- If `nums[mid] > nums[right]`: There's a rotation in the right portion, so the minimum must be there

## Solution

```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            if nums[right] > nums[mid]:
                # Right half is sorted, minimum is in left half (including mid)
                right = mid
            else:
                # Rotation in right half, minimum is there (excluding mid)
                left = mid + 1
        
        return nums[left]
```

## Visual Intuition

```
Case 1: nums[mid] < nums[right] - Right side sorted, search left
[4, 5, 6, 7, 0, 1, 2]
 L        M        R
 mid=7, right=2
 7 > 2? No → Rotation in right half
 
[4, 5, 6, 7, 0, 1, 2]
          L  M     R
 mid=0, right=2
 0 < 2? Yes → Right sorted, search left (include mid)

[4, 5, 6, 7, 0, 1, 2]
          L/M/R
 Found minimum: 0

Case 2: Array not rotated
[1, 2, 3, 4, 5]
 L     M     R
 mid=3, right=5
 3 < 5? Yes → Right sorted, search left
 
[1, 2, 3]
 L  M  R
 mid=2, right=3
 2 < 3? Yes → Right sorted, search left

[1, 2]
 L  R
 M
 mid=1, right=2
 1 < 2? Yes → Right sorted, search left

[1]
L/R
Found minimum: 1
```

## Why Right Comparison Works

### The Property We're Exploiting
In a properly sorted segment (no rotation), the rightmost element is always greater than any element in that segment. So:
- If `nums[mid] < nums[right]`: The segment [mid...right] is properly sorted
- If `nums[mid] > nums[right]`: There's a "break" (rotation point) between mid and right

### Why Not Compare with Left?

Comparing with left has a critical edge case:

```python
# Unrotated array: [1, 2, 3, 4, 5]
left = 0, right = 4, mid = 2
nums[left] = 1, nums[mid] = 3

nums[left] < nums[mid]? Yes (1 < 3)
# But we can't conclude minimum is in right half!
# The minimum is actually at left (1)
```

The problem is that `nums[left] < nums[mid]` is true for both:
1. Normal sorted segment (no rotation)
2. Left segment of a rotated array

This ambiguity makes left comparison unreliable.

### Right Comparison is Unambiguous

```python
# For any segment [mid...right]:
if nums[mid] < nums[right]:
    # DEFINITELY properly sorted (no rotation)
    # Minimum cannot be in (mid, right]
else:
    # DEFINITELY has rotation
    # Minimum must be in (mid, right]
```

## Key Observations

1. **Why `right = mid` not `right = mid - 1`?**
   - When right half is sorted, mid itself could be the minimum
   - Example: [2, 1] → mid=2, right=1, we need to include mid

2. **Why `left = mid + 1` not `left = mid`?**
   - When rotation is in right half, mid cannot be minimum (it's greater than something to its right)
   - We can safely exclude mid

3. **Edge Cases Handled:**
   - Single element: Direct return
   - No rotation: Works correctly by always searching left
   - Fully rotated (n times): Same as no rotation

## Complexity Analysis

- **Time Complexity:** O(log n) - Binary search halving the search space each iteration
- **Space Complexity:** O(1) - Only using a few variables

## Alternative Approach: Direct Rotation Check

```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        # If array is not rotated
        if nums[left] < nums[right]:
            return nums[left]
        
        while left < right:
            mid = (left + right) // 2
            
            # Found the rotation point
            if mid > 0 and nums[mid] < nums[mid - 1]:
                return nums[mid]
            if mid < len(nums) - 1 and nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            
            # Decide which half to search
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        return nums[left]
```

This approach explicitly checks for the rotation point but requires more comparisons.

## Pattern Recognition

This problem demonstrates:
- **Binary Search on Rotated Array** - Using comparison with endpoints to determine sorted portions
- **Invariant Maintenance** - The minimum always stays within [left, right]
- **Property Exploitation** - Using the sorted property to eliminate half the search space

## What I Learned

The elegance of comparing with the right pointer lies in its definitiveness. While comparing with the left pointer creates ambiguity (sorted segment vs. rotated array's left portion), the right comparison gives us certain knowledge about where the rotation point must be. This is a beautiful example of choosing the right invariant to make the algorithm both correct and simple.

The pattern of `right = mid` vs `left = mid + 1` also taught me to think carefully about boundary inclusion based on what we can deduce from our comparisons.