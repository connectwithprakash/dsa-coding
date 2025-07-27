# 3Sum

## Problem Statement
Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

Notice that the solution set must not contain duplicate triplets.

## Examples
```
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
```

## My Approach
I'll treat this as **n different two-sum problems**:

1. **Sort the array** - Enables two-pointer technique and easy duplicate handling
2. **For each number as first element** - Fix one number, find pairs that sum to its negative
3. **Use two pointers** - For remaining elements, find two-sum using two pointers
4. **Skip duplicates** - Avoid duplicate triplets

**Key insight**: Fix the first element, then solve Two Sum II for the remaining array!

## My Original Solution (With Issues)
```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the numbers O(nlog(n))
        nums = sorted(nums)
        n = len(nums)

        triplets = set()
        # Use two pointers for each pointer (3rd pointer)
        for idx in range(n):
            head, tail = 0, n-1
            target = -nums[idx]
            while head < tail:
                if head == idx:
                    head += 1
                    continue
                elif tail == idx:
                    tail -= 1
                    continue
                else:
                    pass
                
                sum_ = nums[head]+nums[tail]
                if sum_ < target:
                    head += 1
                elif sum_ > target:
                    tail -= 1
                else:
                    if idx < head:
                        triplet = (nums[idx], nums[head], nums[tail])
                    elif head < idx < tail:
                        triplet = (nums[head], nums[idx], nums[tail])
                    else:
                        triplet = (nums[head], nums[tail], nums[idx])
                    head += 1
                    triplets.add(triplet)
        return [list(triplet) for triplet in triplets]
```

## Issues in My Original Approach
1. **Complex index handling** - Managing three overlapping pointers is messy
2. **Inefficient duplicate skipping** - Using set() works but not optimal
3. **Tuple ordering logic** - Complex conditional logic for maintaining sorted order

## My Final Solution
```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the numbers O(nlog(n))
        nums = sorted(nums)
        # -4, -1, -1, 0, 1, 2
        n = len(nums)

        triplets = []
        for idx in range(n-2):
            # Skip duplicates for first element
            # idx > 0 ensures we don't skip the very first element (no previous element to compare)
            if idx > 0 and nums[idx] == nums[idx-1]:
                continue
            
            jdx, kdx = idx+1, n-1
            while jdx < kdx:
                three_sum = nums[idx] + nums[jdx] + nums[kdx]
                if three_sum < 0:
                    jdx += 1
                elif three_sum > 0:
                    kdx -= 1
                else:
                    triplets.append([nums[idx], nums[jdx], nums[kdx]])
                    jdx += 1
                    kdx -= 1
                    # Skip duplicates for second element after finding a valid triplet
                    # This prevents duplicate triplets like [-1,0,1] being added multiple times
                    while (nums[jdx] == nums[jdx-1]) and (jdx<kdx):
                        jdx += 1
                    
        return triplets
```

## Complexity Analysis ✅
- **Time Complexity**: O(n²) - O(n log n) sorting + O(n) * O(n) two-pointer loops
- **Space Complexity**: O(1) - Only using constant extra space (not counting output)

**Perfect! Meets both requirements** ✅

## Example Walkthrough
**Input**: `nums = [-1,0,1,2,-1,-4]`
**After sorting**: `[-4,-1,-1,0,1,2]`

**Process**:
1. **i=0, nums[i]=-4, target=4**:
   - left=1(-1), right=5(2) → sum=-1+2=1 < 4 → move left
   - left=2(-1), right=5(2) → sum=-1+2=1 < 4 → move left
   - left=3(0), right=5(2) → sum=0+2=2 < 4 → move left
   - left=4(1), right=5(2) → sum=1+2=3 < 4 → move left
   - left=5, right=5 → end

2. **i=1, nums[i]=-1, target=1**:
   - left=2(-1), right=5(2) → sum=-1+2=1 = 1 → **Found: [-1,-1,2]** ✅
   - Skip duplicates, continue...
   - left=3(0), right=4(1) → sum=0+1=1 = 1 → **Found: [-1,0,1]** ✅

3. **i=2, nums[i]=-1**: Skip (duplicate of previous)

**Result**: `[[-1,-1,2], [-1,0,1]]` ✅

## What I Learned From This Problem

### Key Insights I Learned
- **Fix the first element** - Makes the problem simpler by reducing to Two Sum
- **Why `idx > 0`**: Prevents skipping the very first element since there's no previous element to compare
- **Duplicate skipping strategy**: Only skip duplicates for the second element after finding a valid triplet
- **Natural ordering**: Since array is sorted and `jdx > idx`, triplets are naturally ordered

## Complexity Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Brute Force** | O(n³) | O(1) | Check all possible triplets |
| **Hash Set** | O(n²) | O(n) | Fix two elements, lookup third |
| **My Optimized** | O(n²) | O(1) | Sort + fix first + two pointers |

## Why This Approach is Optimal
1. **Leverages sorting** - Enables two-pointer technique and easy duplicate handling
2. **Reduces to known problem** - Each iteration is a Two Sum II problem  
3. **Natural duplicate avoidance** - No need for complex set operations
4. **Clear logic flow** - Easy to understand and debug

