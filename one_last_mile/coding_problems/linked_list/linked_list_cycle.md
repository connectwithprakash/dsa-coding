# Linked List Cycle

## Problem
Given `head`, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer.

Return `true` if there is a cycle in the linked list. Otherwise, return `false`.

## My Approaches

I came up with two different approaches - one creative value modification approach and the classic Floyd's algorithm.

### Approach 1: Value Modification (Creative)

```python
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        while head:
            if head.val > 1000:
                return True
            else:
                head.val += 1000
            head = head.next
        
        return False
```

This approach leverages the constraint that node values are in range [-10^5, 10^5]. By adding 1000 to visited nodes, I can detect if we've seen a node before without using extra space for a hash set.

### Approach 2: Floyd's Cycle Detection (Two Pointers)

```python
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        
        return False
```

The classic tortoise and hare algorithm - if there's a cycle, the fast pointer will eventually catch up to the slow pointer.

## Visual Intuition

### How Floyd's Algorithm Works

```
No Cycle Case:
1 → 2 → 3 → 4 → None

Step 1: slow=1, fast=1
Step 2: slow=2, fast=3
Step 3: slow=3, fast=None (fast.next is None, exit)
Return: False

Cycle Case:
1 → 2 → 3 → 4
    ↑       ↓
    └───────┘

Step 1: slow=1, fast=1
Step 2: slow=2, fast=3
Step 3: slow=3, fast=2 (fast went 4→2)
Step 4: slow=4, fast=4 (slow and fast meet!)
Return: True
```

### Why Floyd's Algorithm Works

If there's a cycle:
- The fast pointer enters the cycle first
- Once both pointers are in the cycle, the fast pointer gains on the slow pointer by 1 node per iteration
- Since the gap decreases by 1 each time, they must eventually meet

Mathematical proof:
- Let the cycle length be `L`
- When slow enters the cycle, fast is already `k` nodes ahead (where k < L)
- The gap between them is `L - k`
- Gap decreases by 1 each iteration: (L-k), (L-k-1), ..., 1, 0
- They meet when gap = 0

## Complexity Analysis

### Value Modification Approach
- **Time Complexity:** O(n) - Visit each node once
- **Space Complexity:** O(1) - No extra space
- **Drawback:** Modifies the input list

### Floyd's Algorithm
- **Time Complexity:** O(n) - In worst case, traverse the list twice
- **Space Complexity:** O(1) - Only two pointers
- **Advantage:** Doesn't modify the input

## Alternative: HashSet Approach

```python
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        
        while head:
            if head in visited:
                return True
            visited.add(head)
            head = head.next
        
        return False
```

- **Time:** O(n)
- **Space:** O(n) - Stores all nodes in set

## Edge Cases

```python
# Edge Case 1: Empty list
head = None
# Returns: False

# Edge Case 2: Single node, no cycle
head = ListNode(1)
# Returns: False

# Edge Case 3: Single node with self-cycle
head = ListNode(1)
head.next = head
# Returns: True

# Edge Case 4: Two nodes with cycle
head = ListNode(1)
head.next = ListNode(2)
head.next.next = head
# Returns: True
```

## Key Insights

1. **Floyd's algorithm is optimal** - O(n) time with O(1) space without modifying input

2. **Creative solutions exist** - My value modification approach shows thinking outside the box, though it has the drawback of modifying input

3. **Meeting point guaranteed** - In Floyd's algorithm, if there's a cycle, the pointers MUST meet (mathematical certainty)

4. **Different speeds work** - The fast pointer could move 3, 4, or k steps - as long as speeds differ, they'll meet in a cycle

## Common Mistakes

1. **Off-by-one initialization**:
   ```python
   # My initial attempt (works but less clean):
   slow = head
   fast = head.next  # Different starting points
   
   # Better:
   slow = fast = head  # Same starting point
   ```

2. **Forgetting null checks**:
   ```python
   # Wrong: Doesn't check fast.next
   while fast:
       fast = fast.next.next  # Could crash!
   
   # Correct:
   while fast and fast.next:
       fast = fast.next.next
   ```

3. **Checking before moving**:
   ```python
   # Wrong: Check before moving
   while fast and fast.next:
       if slow == fast:  # They start equal!
           return True
       slow = slow.next
       fast = fast.next.next
   
   # Correct: Move first, then check
   ```

## Pattern Recognition

Floyd's Cycle Detection appears in:
- Find the start of cycle (Linked List Cycle II)
- Find duplicate number in array
- Happy Number problem
- Detect cycle in directed graph

## What I Learned

The Floyd's algorithm is elegant in its simplicity - just two pointers moving at different speeds. My creative value modification approach worked but highlighted the importance of considering whether modifying input is acceptable. The mathematical guarantee that pointers will meet in a cycle is fascinating - it's not just probable, it's certain!