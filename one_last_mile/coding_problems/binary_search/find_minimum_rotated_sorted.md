# Find Minimum in Rotated Sorted Array

## Problem
Suppose an array of length `n` sorted in ascending order is rotated between `1` and `n` times. For example, the array `nums = [0,1,2,4,5,6,7]` might become:
- `[4,5,6,7,0,1,2]` if it was rotated 4 times
- `[0,1,2,4,5,6,7]` if it was rotated 7 times (back to original)

Given the sorted rotated array `nums` of unique elements, return the minimum element of this array.

You must write an algorithm that runs in `O(log n)` time.

## My Approach

The key insight I had was recognizing that in a rotated sorted array, one half is always properly sorted. By comparing the middle element with the right element, I can determine which half contains the rotation point (minimum element).

### Why Compare with Right, Not Left?

The key realization is about what each comparison tells us:

**Comparing with right (✓ Works reliably):**
- If `nums[mid] < nums[right]`: The segment [mid...right] is properly sorted ascending, which means this segment has no rotation point. The minimum must be at mid or to its left.
- If `nums[mid] > nums[right]`: There's a "drop" between mid and right (like 7→1), meaning the rotation point (minimum) is definitely in (mid...right].

**Comparing with left (✗ Doesn't work reliably):**
- If `nums[left] < nums[mid]`: The segment [left...mid] is sorted, but this doesn't tell us where the minimum is! 
  - Example 1: `[3,4,5,1,2]` - left(3) < mid(5), minimum is in right half
  - Example 2: `[5,1,2,3,4]` - left(5) > mid(2), minimum is in left half  
  - Example 3: `[1,2,3,4,5]` - left(1) < mid(3), minimum is in left half
  
The problem: When [left...mid] is sorted, the minimum could be `nums[left]` itself (if no rotation or rotation brought it to front), making it impossible to decide which half to discard.

**The fundamental difference:**
- Right comparison: A sorted right segment guarantees no minimum there (except possibly mid)
- Left comparison: A sorted left segment could still contain the minimum at its start

## Solution

```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            # If mid element is less than right element,
            # right half is sorted, minimum is in left half (including mid)
            if nums[mid] < nums[right]:
                right = mid
            # Otherwise, left half is sorted,
            # minimum is in right half (excluding mid)
            else:
                left = mid + 1
        
        return nums[left]
```

## Visual Intuition

```
Example 1: [3, 4, 5, 6, 1, 2]

Step 1: left=0, right=5, mid=2
        [3, 4, 5, 6, 1, 2]
         L     M        R
        nums[2]=5 > nums[5]=2
        Left half sorted, min in right half
        left = mid + 1 = 3

Step 2: left=3, right=5, mid=4
        [3, 4, 5, 6, 1, 2]
                  L  M  R
        nums[4]=1 < nums[5]=2
        Right half sorted, min in left half
        right = mid = 4

Step 3: left=3, right=4, mid=3
        [3, 4, 5, 6, 1, 2]
                  L  R
                  M
        nums[3]=6 > nums[4]=1
        left = mid + 1 = 4

Step 4: left=4, right=4
        Return nums[4] = 1 ✓

Example 2: [4, 5, 6, 7] (no rotation)

Step 1: left=0, right=3, mid=1
        [4, 5, 6, 7]
         L  M     R
        nums[1]=5 < nums[3]=7
        Right half sorted, min in left half
        right = mid = 1

Step 2: left=0, right=1, mid=0
        [4, 5]
         L  R
         M
        nums[0]=4 < nums[1]=5
        right = mid = 0

Step 3: left=0, right=0
        Return nums[0] = 4 ✓
```

## Why the Algorithm Works

### Case Analysis

**Case 1: `nums[mid] < nums[right]`**
```
    /
   /
  /
mid  right
```
The right portion is properly sorted. The minimum cannot be in the right portion (except possibly at mid), so we search left including mid.

**Case 2: `nums[mid] > nums[right]`**
```
      mid
       /
      /
     /
        right
```
There's a rotation point between mid and right. The minimum must be in the right portion (excluding mid since it's larger than right).

### Concrete Example: Why Left Comparison Fails

Consider these arrays with mid at index 2:

**Using LEFT comparison (problematic):**
```
[1, 2, 3, 4, 5]  left(1) < mid(3) → left sorted, but min is at left!
[2, 3, 4, 5, 1]  left(2) < mid(4) → left sorted, but min is at right!
[4, 5, 1, 2, 3]  left(4) > mid(1) → break in left, min is at mid
```
When left < mid (left segment sorted), we cannot determine where minimum is!

**Using RIGHT comparison (reliable):**
```
[1, 2, 3, 4, 5]  mid(3) < right(5) → right sorted, min must be left/mid ✓
[2, 3, 4, 5, 1]  mid(4) > right(1) → break in right, min must be right ✓  
[4, 5, 1, 2, 3]  mid(1) < right(3) → right sorted, min must be left/mid ✓
```
The right comparison always tells us definitively which half to search!

## Complexity Analysis

- **Time Complexity:** O(log n)
  - Binary search with each iteration halving the search space
  
- **Space Complexity:** O(1)
  - Only using pointers, no additional data structures

## Edge Cases

1. **Single element:** `[1]` → return 1
2. **Two elements:** `[2, 1]` → return 1
3. **No rotation:** `[1, 2, 3, 4, 5]` → return 1
4. **Full rotation:** Array back to original order
5. **Minimum at boundaries:** First or last element

## Key Insights

1. **Rotation property** - One half is always sorted in a rotated array
2. **Right comparison** - More reliable than left for finding rotation point
3. **Include mid when moving right** - Mid might be the minimum
4. **Exclude mid when moving left** - Mid is definitely not the minimum

## Common Pitfalls

1. **Wrong comparison** - Using left instead of right for comparison
2. **Boundary handling** - Not including mid when setting `right = mid`
3. **Off-by-one** - Using `left <= right` instead of `left < right`

## Pattern Recognition

This problem demonstrates:
- **Modified Binary Search** - Binary search with rotation handling
- **Sorted array property** - Leveraging partially sorted nature
- **Invariant maintenance** - Minimum always in [left, right] range

## Related Problems

- Search in Rotated Sorted Array (find target instead of minimum)
- Find Minimum in Rotated Sorted Array II (with duplicates)
- Search in Rotated Sorted Array II (with duplicates)

## What I Learned

The elegance of this solution is in recognizing that we don't need to find the exact rotation point - we just need to narrow down to the minimum. The comparison with the right element reliably tells us which half to discard. This taught me that sometimes the choice of comparison point (left vs right) can make the difference between a working and non-working algorithm.