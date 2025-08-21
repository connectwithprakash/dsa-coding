# Reorder List

## Problem
You are given the head of a singly linked list. The list can be represented as:
L0 → L1 → ... → Ln-1 → Ln

Reorder the list to be in the following form:
L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → ...

You may not modify the values in the list's nodes. Only nodes themselves may be changed.

## My Approach

I realized this problem requires three steps:
1. Find the middle of the list to split it into two halves
2. Reverse the second half
3. Merge the two halves by alternating nodes

This combines three fundamental linked list patterns I've already learned!

## Solution with Comments

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Step 1: Find the middle of the linked list using slow-fast pointers
        # Slow moves 1 step, fast moves 2 steps
        # When fast reaches end, slow is at middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Split the list and reverse the second half
        # Save the start of second half
        second_half = slow.next
        prev = None
        # Cut the connection between first and second half
        slow.next = None
        
        # Reverse the second half using three-pointer technique
        current = second_half
        while current:
            temp = current.next  # Save next node
            current.next = prev  # Reverse the pointer
            prev = current        # Move prev forward
            current = temp        # Move to next node
        
        # Step 3: Merge the two halves alternately
        # prev now points to the head of reversed second half
        first_half = head
        second_half = prev
        
        # Merge by taking one from first, then one from second
        # Second half is always shorter or equal in length
        while second_half:
            # Save the next nodes before we break the links
            first_next = first_half.next
            second_next = second_half.next
            
            # Connect first to second
            first_half.next = second_half
            # Connect second to the saved first_next
            second_half.next = first_next
            
            # Move pointers forward
            first_half = first_next
            second_half = second_next
```

## Visual Intuition

### Example 1: Even Length List [1,2,3,4]

```
Original: 1 → 2 → 3 → 4 → None

Step 1 - Find Middle:
slow/fast: slow=1, fast=2
          slow=2, fast=4
Middle found at node 2

Step 2 - Split and Reverse:
First half:  1 → 2 → None
Second half: 3 → 4 → None
After reversing second: 4 → 3 → None

Step 3 - Merge Alternately:
Initial: first=1, second=4

Iteration 1:
  Save: first_next=2, second_next=3
  Link: 1→4, 4→2
  Move: first=2, second=3
  
Iteration 2:
  Save: first_next=None, second_next=None
  Link: 2→3, 3→None
  Move: first=None, second=None

Result: 1 → 4 → 2 → 3 → None ✓
```

### Example 2: Odd Length List [1,2,3,4,5]

```
Original: 1 → 2 → 3 → 4 → 5 → None

Step 1 - Find Middle:
slow/fast: slow=1, fast=2
          slow=2, fast=4
          slow=3, fast=None
Middle found at node 3

Step 2 - Split and Reverse:
First half:  1 → 2 → 3 → None
Second half: 4 → 5 → None
After reversing second: 5 → 4 → None

Step 3 - Merge Alternately:
Iteration 1: 1→5→2
Iteration 2: 2→4→3
(second_half becomes None, exit)

Result: 1 → 5 → 2 → 4 → 3 → None ✓
```

## Why This Works

The algorithm leverages three key insights:

1. **Middle splitting ensures correct interleaving**: The first half has either equal or one more node than the second half, perfect for alternating

2. **Reversing second half aligns last with first**: After reversal, we can easily pair L0 with Ln, L1 with Ln-1, etc.

3. **Merging while second exists handles both cases**: Since second half is never longer, we only need to check if it has nodes

## Complexity Analysis

- **Time Complexity:** O(n)
  - Finding middle: O(n/2)
  - Reversing second half: O(n/2)
  - Merging: O(n/2)
  - Total: O(n)

- **Space Complexity:** O(1)
  - Only using a constant number of pointers
  - Modifying links in-place

## Edge Cases

```python
# Edge Case 1: Single node
[1] → [1] (no change needed)

# Edge Case 2: Two nodes  
[1,2] → [1,2] (already in correct order)

# Edge Case 3: Three nodes
[1,2,3] → [1,3,2]

# Edge Case 4: Empty list
[] → [] (though problem guarantees at least 1 node)
```

## Key Insights

1. **Composition of patterns** - This problem beautifully combines three fundamental operations: finding middle, reversing, and merging

2. **Slow-fast pointer precision** - Starting fast at head.next (not head) ensures slow stops at the right position for splitting

3. **In-place manipulation** - No new nodes created, just rewiring existing pointers

4. **Order preservation** - The relative order within each half is maintained, only the halves are interleaved

## Common Mistakes

1. **Wrong middle for even-length lists**:
   ```python
   # Wrong: Starting both at head
   slow = fast = head  # Slow ends one position too far
   
   # Correct: Fast starts at head.next
   slow, fast = head, head.next
   ```

2. **Forgetting to cut the connection**:
   ```python
   # Wrong: Not disconnecting first and second half
   second = slow.next
   # Missing: slow.next = None
   ```

3. **Incorrect merge termination**:
   ```python
   # Wrong: Checking first_half
   while first_half:  # First half might be longer!
   
   # Correct: Check second_half
   while second_half:  # Second is never longer
   ```

## Pattern Recognition

This problem combines three patterns:
1. **Find Middle** - Slow/fast pointers (from finding cycle start)
2. **Reverse List** - Three-pointer reversal (from Reverse Linked List)
3. **Merge Lists** - Alternating merge (variation of Merge Two Sorted Lists)

Similar problems that use these combinations:
- Palindrome Linked List (find middle + reverse + compare)
- Sort List (find middle + merge sort)
- Rotate List (find length + reconnect)

## What I Learned

This problem is a perfect example of how complex linked list problems are really just combinations of simpler patterns. By mastering the basic operations (reverse, find middle, merge), I can tackle seemingly complex problems by breaking them down into familiar steps. The key insight was recognizing that reordering L0→Ln→L1→Ln-1 is essentially merging the first half with the reversed second half!