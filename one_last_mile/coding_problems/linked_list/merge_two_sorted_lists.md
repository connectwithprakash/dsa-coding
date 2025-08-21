# Merge Two Sorted Lists

## Problem
You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

## My Approach

I used the dummy node pattern to simplify the merge logic. By maintaining a current pointer that builds the merged list one node at a time, I can compare values and attach the smaller node. When one list is exhausted, I attach the remainder of the other list.

## Solution

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy node to simplify edge cases
        head = ListNode(0)
        curr = head
        
        while True:
            if list1 and list2:
                # Both lists have elements, choose smaller
                if list1.val > list2.val:
                    curr.next = list2
                    list2 = list2.next
                else:
                    curr.next = list1
                    list1 = list1.next
                curr = curr.next
            elif list1:
                # list2 exhausted, attach rest of list1
                curr.next = list1
                break
            elif list2:
                # list1 exhausted, attach rest of list2
                curr.next = list2
                break
            else:
                # Both lists empty/exhausted
                break
        
        return head.next  # Skip dummy node
```

## Visual Intuition

```
Example: Merge [1,2,4] and [1,3,5]

Initial:
list1: 1 → 2 → 4 → None
       ↑
list2: 1 → 3 → 5 → None
       ↑
dummy: 0 →
       ↑
      curr

Step 1: Compare 1 and 1, take from list1 (equal values)
list1: 1 → 2 → 4 → None
           ↑
list2: 1 → 3 → 5 → None
       ↑
dummy: 0 → 1 →
           ↑
          curr

Step 2: Compare 2 and 1, take from list2
list1: 1 → 2 → 4 → None
           ↑
list2: 1 → 3 → 5 → None
           ↑
dummy: 0 → 1 → 1 →
               ↑
              curr

Step 3: Compare 2 and 3, take from list1
list1: 1 → 2 → 4 → None
               ↑
list2: 1 → 3 → 5 → None
           ↑
dummy: 0 → 1 → 1 → 2 →
                   ↑
                  curr

Step 4: Compare 4 and 3, take from list2
list1: 1 → 2 → 4 → None
               ↑
list2: 1 → 3 → 5 → None
               ↑
dummy: 0 → 1 → 1 → 2 → 3 →
                       ↑
                      curr

Step 5: Compare 4 and 5, take from list1
list1: 1 → 2 → 4 → None
                   ↑
list2: 1 → 3 → 5 → None
               ↑
dummy: 0 → 1 → 1 → 2 → 3 → 4 →
                           ↑
                          curr

Step 6: list1 exhausted, attach rest of list2
dummy: 0 → 1 → 1 → 2 → 3 → 4 → 5 → None

Return: head.next (skip dummy)
Result: 1 → 1 → 2 → 3 → 4 → 5 → None
```

## Alternative: Cleaner While Condition

```python
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        
        # Process while both lists have elements
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        
        # Attach remaining elements (at most one list has elements)
        curr.next = list1 if list1 else list2
        
        return dummy.next
```

## Recursive Solution

```python
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Base cases
        if not list1:
            return list2
        if not list2:
            return list1
        
        # Recursive merge
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
```

## Complexity Analysis

### Iterative (My Solution)
- **Time Complexity:** O(m + n) where m and n are lengths of the lists
  - Each node is visited exactly once
- **Space Complexity:** O(1)
  - Only using a few pointers

### Recursive
- **Time Complexity:** O(m + n)
- **Space Complexity:** O(m + n)
  - Recursion stack depth

## Edge Cases

```python
# Edge Case 1: Both lists empty
list1 = None, list2 = None
# Returns: None

# Edge Case 2: One list empty
list1 = None, list2 = 1→2→3
# Returns: 1→2→3

# Edge Case 3: Single element lists
list1 = 1→None, list2 = 2→None
# Returns: 1→2→None

# Edge Case 4: Equal elements
list1 = 1→1→1, list2 = 1→1→1
# Returns: 1→1→1→1→1→1 (maintains stability)
```

## Key Insights

1. **Dummy node pattern** - Eliminates special handling for the head of the result list

2. **No new nodes created** - We're splicing existing nodes, just changing pointers

3. **Attach remainder optimization** - When one list is exhausted, we can attach the entire remainder of the other list in O(1)

4. **Stability** - When values are equal, taking from list1 first maintains relative order

## Common Mistakes

1. **Forgetting to advance curr**:
   ```python
   # Wrong: curr doesn't move
   curr.next = list1
   list1 = list1.next
   # Missing: curr = curr.next
   ```

2. **Returning dummy instead of dummy.next**:
   ```python
   # Wrong: Includes dummy node with value 0
   return head
   # Correct: Skip dummy
   return head.next
   ```

3. **Not handling empty lists**:
   ```python
   # Wrong: Assumes lists are non-empty
   if list1.val < list2.val:  # Crashes if list1 is None
   ```

## Pattern Recognition

This problem uses:
- **Two pointer comparison** - Similar to merging in merge sort
- **Dummy node pattern** - Simplifies list construction
- **Splice optimization** - Attach remainder when one exhausted

Similar problems:
- Merge k Sorted Lists (extension to k lists)
- Sort List (uses merge as subroutine)
- Merge Sorted Array (array version)

## What I Learned

The dummy node pattern is incredibly powerful for list construction problems. It eliminates all the edge cases around handling the first node specially. The optimization of attaching the remainder when one list is exhausted is a nice touch that works because the lists are already sorted. This merge operation is the foundation of merge sort on linked lists.