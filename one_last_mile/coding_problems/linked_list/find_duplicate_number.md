# Find the Duplicate Number

## Problem
Given an array of integers `nums` containing `n + 1` integers where each integer is in the range `[1, n]` inclusive.

There is only one repeated number in `nums`, return this repeated number.

You must solve the problem without modifying the array `nums` and uses only constant extra space.

## My Approach

I realized that since all numbers are in range [1, n], I can use each value as an index into the array itself. By marking visited indices with negative values, I create an implicit hash set without extra space.

## Solution - Array as Hash Set

```python
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Use array values as indices
        # Mark visited indices by making their values negative
        for idx in range(len(nums)):
            # Get the index this value points to (convert to 0-indexed)
            jdx = abs(nums[idx]) - 1
            
            # If the value at this index is already negative,
            # we've seen this index before - found duplicate!
            if nums[jdx] < 0:
                return abs(nums[idx])
            else:
                # Mark this index as visited
                nums[jdx] *= -1
```

## Visual Intuition

```
Example: nums = [1,3,4,2,2]

Initial: [1, 3, 4, 2, 2]
         idx: 0  1  2  3  4

Step 1: idx=0, val=1, jdx=0
        Check nums[0]=1 (positive)
        Mark: [-1, 3, 4, 2, 2]

Step 2: idx=1, val=3, jdx=2
        Check nums[2]=4 (positive)
        Mark: [-1, 3, -4, 2, 2]

Step 3: idx=2, val=-4, abs(val)=4, jdx=3
        Check nums[3]=2 (positive)
        Mark: [-1, 3, -4, -2, 2]

Step 4: idx=3, val=-2, abs(val)=2, jdx=1
        Check nums[1]=3 (positive)
        Mark: [-1, -3, -4, -2, 2]

Step 5: idx=4, val=2, jdx=1
        Check nums[1]=-3 (NEGATIVE!)
        Found duplicate: return 2
```

## Why This Works

The key insights:
1. **Values as pointers**: Each value in range [1, n] can be used as an index
2. **Negative marking**: We mark visited indices without losing original information (can recover with abs())
3. **Duplicate detection**: When we encounter a value that points to an already-marked index, we've found our duplicate

## Alternative Solution - Floyd's Cycle Detection

Since this problem can be viewed as a linked list with a cycle (where array indices are nodes and values are next pointers), we can also use Floyd's algorithm:

```python
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Phase 1: Find intersection point in cycle
        slow = fast = nums[0]
        
        # Move until they meet (guaranteed due to duplicate)
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        # Phase 2: Find entrance to cycle (the duplicate)
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow
```

### Floyd's Algorithm Visualization

```
Array as implicit linked list:
nums = [1,3,4,2,2]
Index:  0 1 2 3 4

Connections (index → value → next index):
0 → 1 → 3 → 2 → 4 → 2 (cycle!)
        ↑_______|

Phase 1 - Find cycle:
slow: 0→1→3→2→4→2→4→2
fast: 0→1→2→2→2→2
Meet at: 2

Phase 2 - Find entrance:
slow: 0→1→3→2
fast: 2→4→2→4
Meet at: 2 (the duplicate)
```

## Complexity Analysis

### My Solution (Array Marking)
- **Time Complexity:** O(n)
  - Single pass through the array
- **Space Complexity:** O(1) 
  - Modifies input array but no extra space
- **Note:** This technically modifies the array (violates constraint)

### Floyd's Cycle Detection
- **Time Complexity:** O(n)
  - Two phases, each at most n steps
- **Space Complexity:** O(1)
  - Only two pointers
- **Advantage:** Doesn't modify the input array

## Edge Cases

```python
# Edge Case 1: Duplicate is 1
nums = [1,1]
# Both solutions correctly return 1

# Edge Case 2: Duplicate appears multiple times
nums = [2,2,2,2,2]
# Find first occurrence

# Edge Case 3: Large array with duplicate at end
nums = [1,2,3,4,5,6,7,8,9,9]
# Both handle efficiently
```

## Key Insights

1. **Array as implicit data structure** - When values are bounded by array size, the array itself can serve as storage

2. **Negative marking pattern** - Using sign to store boolean state while preserving original value

3. **Problem transformation** - Viewing the array as a linked list reveals the cycle detection approach

4. **Space-time tradeoffs** - My solution trades array modification for simplicity, Floyd's preserves input

## Common Mistakes

1. **Forgetting abs() when accessing**:
   ```python
   # Wrong: Uses negative index
   jdx = nums[idx] - 1  
   
   # Correct: Always use absolute value
   jdx = abs(nums[idx]) - 1
   ```

2. **Not handling already-negative values**:
   ```python
   # Wrong: Doesn't check current value's sign
   if nums[nums[idx]-1] < 0:
   
   # Correct: Use abs() for index calculation
   if nums[abs(nums[idx])-1] < 0:
   ```

3. **Off-by-one with 1-indexed values**:
   ```python
   # Wrong: Forgets to convert to 0-indexed
   jdx = abs(nums[idx])
   
   # Correct: Subtract 1 for 0-indexing
   jdx = abs(nums[idx]) - 1
   ```

## Pattern Recognition

This problem demonstrates:
- **Index manipulation** - Using values as indices when bounded
- **In-place marking** - Modifying array to track state
- **Cycle detection** - Finding duplicates through graph cycles

Similar problems:
- First Missing Positive (uses similar marking)
- Linked List Cycle II (same Floyd's algorithm)
- Set Mismatch (find duplicate and missing)
- Find All Duplicates in Array (multiple duplicates)

## What I Learned

My initial approach of using the array as its own hash set is clever but violates the "don't modify array" constraint. The Floyd's cycle detection approach is brilliant - it treats the array as an implicit linked list where each value points to the next index. Since there's a duplicate, there must be two indices pointing to the same position, creating a cycle. The duplicate number is the entry point of this cycle! This shows how sometimes reframing a problem (array → linked list) reveals elegant solutions.