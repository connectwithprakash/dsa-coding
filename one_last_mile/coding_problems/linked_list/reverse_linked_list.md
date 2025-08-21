# Reverse Linked List

## Problem
Given the `head` of a singly linked list, reverse the list, and return the reversed list.

## My Approach

The key insight I had was that we need to reverse the direction of each pointer while traversing. To do this without losing references, I save the next node before changing the current node's pointer. Then I advance all three pointers (prev, curr, and the saved next) in lockstep.

## Solution

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        
        while curr:
            # Save next node before we break the link
            temp = curr.next
            # Reverse the pointer
            curr.next = prev
            # Move prev and curr one step forward
            prev = curr
            curr = temp
        
        # prev is now the new head
        return prev
```

## Visual Intuition

```
Initial List: 1 → 2 → 3 → 4 → None

Step-by-step reversal:

Start:     prev  curr
            ↓     ↓
           None   1 → 2 → 3 → 4 → None

Step 1:    Save temp = 2
           1.next = None
           Move pointers
                 prev curr
                  ↓    ↓
           None ← 1    2 → 3 → 4 → None

Step 2:    Save temp = 3
           2.next = 1
           Move pointers
                      prev curr
                       ↓    ↓
           None ← 1 ← 2    3 → 4 → None

Step 3:    Save temp = 4
           3.next = 2
           Move pointers
                           prev curr
                            ↓    ↓
           None ← 1 ← 2 ← 3    4 → None

Step 4:    Save temp = None
           4.next = 3
           Move pointers
                                prev curr
                                 ↓    ↓
           None ← 1 ← 2 ← 3 ← 4    None

End:       Return prev (which points to 4)
           Result: 4 → 3 → 2 → 1 → None
```

## Why This Works

The algorithm maintains three references at each step:
1. **prev**: The already-reversed portion of the list
2. **curr**: The node we're currently processing
3. **temp**: The next node to process (saved before we break curr.next)

Each iteration:
- Reverses one link (curr.next = prev)
- Advances the boundary between reversed and unreversed portions

## Alternative: Recursive Solution

```python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: empty list or single node
        if not head or not head.next:
            return head
        
        # Recursively reverse the rest
        new_head = self.reverseList(head.next)
        
        # Reverse the link between head and head.next
        # head.next still points to the last node of reversed sublist
        head.next.next = head
        head.next = None
        
        return new_head
```

### Recursive Visualization
```
reverseList(1→2→3→None)
  ├─ reverseList(2→3→None)
  │    ├─ reverseList(3→None)
  │    │    └─ return 3 (base case)
  │    ├─ 3.next = 2
  │    ├─ 2.next = None
  │    └─ return 3
  ├─ 2.next = 1
  ├─ 1.next = None
  └─ return 3

Result: 3→2→1→None
```

## Complexity Analysis

### Iterative Solution (My Approach)
- **Time Complexity:** O(n) - Visit each node exactly once
- **Space Complexity:** O(1) - Only use three pointers regardless of list size

### Recursive Solution
- **Time Complexity:** O(n) - Visit each node exactly once
- **Space Complexity:** O(n) - Recursion stack depth equals list length

## Edge Cases

```python
# Edge Case 1: Empty list
head = None
# Returns: None

# Edge Case 2: Single node
head = ListNode(1)
# Returns: 1→None (unchanged)

# Edge Case 3: Two nodes
head = 1→2→None
# Returns: 2→1→None
```

## Key Insights

1. **Save before breaking** - Always save curr.next before modifying curr.next = prev

2. **Three-pointer dance** - The synchronized movement of prev, curr, and temp is the heart of the algorithm

3. **prev becomes new head** - After the loop, curr is None and prev points to the last node (new head)

4. **Foundation pattern** - This reversal technique appears in many linked list problems:
   - Palindrome checking (reverse half and compare)
   - Reorder list (reverse second half and merge)
   - Reverse in k-groups (reverse segments)

## Common Mistakes to Avoid

1. **Losing the next node**:
   ```python
   # Wrong: Lost reference to rest of list
   curr.next = prev  # Now curr.next is gone!
   curr = curr.next  # This would be prev, not the original next
   ```

2. **Returning wrong node**:
   ```python
   # Wrong: Returning curr (which is None at the end)
   return curr
   # Correct: Return prev (the new head)
   return prev
   ```

## Pattern Recognition

This problem introduces the fundamental **pointer reversal pattern** used in:
- Reverse Linked List II (reverse portion)
- Palindrome Linked List (reverse and compare)
- Reorder List (reverse second half)
- Add Two Numbers II (reverse, add, reverse)

## What I Learned

The elegance of this solution is in its simplicity - just three pointers moving in lockstep, reversing one link at a time. This iterative approach is superior to recursion for production code due to O(1) space complexity and no stack overflow risk. The pattern of saving a reference before breaking it is crucial in all linked list manipulation.