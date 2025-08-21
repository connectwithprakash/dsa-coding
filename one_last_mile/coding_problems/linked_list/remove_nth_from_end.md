# Remove Nth Node From End of List

## Problem
Given the `head` of a linked list, remove the `nth` node from the end of the list and return its head.

## My Two-Pass Approach

I first find the total length of the list, then calculate which node to remove from the start.

### Solution with Comments

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Step 1: Find total length using slow-fast pointers
        # This is more complex than needed but shows pattern reuse
        length_finder_slow = head
        length_finder_fast = head.next
        
        total_length = 1  # Start with 1 for head node
        
        # Count nodes using slow-fast technique
        while length_finder_fast and length_finder_fast.next:
            total_length += 2  # Fast moves 2 nodes
            length_finder_slow = length_finder_slow.next
            length_finder_fast = length_finder_fast.next.next
        
        # Add 1 if fast is not None (odd length list)
        if length_finder_fast:
            total_length += 1
        
        # Step 2: Calculate position from start
        # To remove nth from end, we need (total - n)th from start
        # But we need the node BEFORE it, so (total - n - 1)
        position_from_start = total_length - n - 1
        
        # Edge case: removing the head node
        # If position is negative, we're removing the first node
        if position_from_start < 0:
            return head.next
        
        # Step 3: Traverse to the node before the target
        current = head
        for _ in range(position_from_start):
            current = current.next
        
        # Step 4: Remove the target node by skipping it
        if current.next:
            current.next = current.next.next
        
        return head
```

## Optimized One-Pass Solution

The elegant approach uses two pointers with a gap of n nodes.

```python
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Dummy node simplifies edge case of removing head
        dummy = ListNode(0, head)
        
        # Initialize two pointers
        left = dummy  # Will end up before node to remove
        right = head  # Will scout ahead by n nodes
        
        # Create a gap of n nodes between left and right
        # Move right pointer n steps ahead
        for _ in range(n):
            right = right.next
        
        # Move both pointers until right reaches the end
        # This maintains the gap of n nodes
        # When right is None, left is before the nth node from end
        while right:
            left = left.next
            right = right.next
        
        # Remove the nth node from end
        # left.next is the node to remove
        left.next = left.next.next
        
        # Return the head (skipping dummy)
        return dummy.next
```

## Visual Intuition

### Example: Remove 2nd from end in [1,2,3,4,5]

#### Two-Pass Approach:
```
Pass 1 - Find Length:
1 → 2 → 3 → 4 → 5 → None
Total length = 5

Calculate: position_from_start = 5 - 2 - 1 = 2

Pass 2 - Remove:
1 → 2 → 3 → 4 → 5
        ↑
     current (after 2 moves)
     
Remove: current.next = current.next.next
Result: 1 → 2 → 3 → 5 → None
```

#### One-Pass Approach:
```
Initial Setup with dummy:
dummy → 1 → 2 → 3 → 4 → 5 → None
  ↑     ↑
 left  right

Create gap of 2:
dummy → 1 → 2 → 3 → 4 → 5 → None
  ↑             ↑
 left         right

Move both until right is None:
Step 1: left=1, right=4
Step 2: left=2, right=5
Step 3: left=3, right=None (stop)

dummy → 1 → 2 → 3 → 4 → 5 → None
                ↑
              left
              
Remove: left.next = left.next.next
Result: 1 → 2 → 3 → 5 → None
```

## Edge Cases

```python
# Edge Case 1: Remove head (n equals list length)
[1,2,3], n=3
# My approach: position = 3-3-1 = -1 < 0, return head.next
# One-pass: dummy helps handle this naturally
Result: [2,3]

# Edge Case 2: Single node
[1], n=1
Result: []

# Edge Case 3: Remove last node
[1,2,3], n=1
Result: [1,2]

# Edge Case 4: Two nodes, remove first
[1,2], n=2
Result: [2]
```

## Complexity Analysis

### Two-Pass Approach (My Solution)
- **Time Complexity:** O(n)
  - First pass to find length: O(n)
  - Second pass to find node: O(n)
  - Total: O(2n) = O(n)
- **Space Complexity:** O(1)

### One-Pass Approach
- **Time Complexity:** O(n)
  - Single traversal with two pointers
- **Space Complexity:** O(1)

## Key Insights

1. **Two-pointer gap technique** - Maintaining a fixed gap between pointers is powerful for "nth from end" problems

2. **Dummy node pattern** - Eliminates special handling for removing the head node

3. **One-pass vs Two-pass trade-off** - My solution is more intuitive but less optimal; the one-pass is elegant but requires the gap insight

4. **Position calculation** - Converting "nth from end" to "position from start" requires careful index math

## Common Mistakes

1. **Off-by-one in position calculation**:
   ```python
   # Wrong: Forgetting we need the node BEFORE target
   position = total_length - n  # Points to target, not predecessor
   
   # Correct: 
   position = total_length - n - 1  # Points to predecessor
   ```

2. **Not handling head removal**:
   ```python
   # Wrong: Crashes when removing head
   current = head
   for _ in range(position_from_start):  # Negative range!
   
   # Correct: Check for negative position first
   if position_from_start < 0:
       return head.next
   ```

3. **Gap creation in one-pass**:
   ```python
   # Wrong: Creating gap of n-1
   for _ in range(n-1):  # Off by one!
   
   # Correct: Gap should be exactly n
   for _ in range(n):
   ```

## Pattern Recognition

This problem demonstrates:
- **Two-pointer with gap** - Maintaining fixed distance between pointers
- **Dummy node** - Simplifying edge cases
- **Length finding** - Can use slow-fast or simple traversal

Similar problems:
- Find middle of linked list (gap = length/2)
- Detect start of cycle (gap technique after finding cycle)
- Rotate list by k (find length, then reconnect)

## What I Learned

My initial solution worked but was more complex than needed. The key insight I missed was the two-pointer gap technique - by maintaining a gap of exactly n nodes, we can find the predecessor of the target node in one pass. The dummy node pattern is also crucial here, as it elegantly handles the edge case of removing the head without special logic. Sometimes the simpler approach (one traversal to count) is clearer than trying to reuse complex patterns (slow-fast for counting).