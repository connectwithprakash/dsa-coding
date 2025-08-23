# Reverse Nodes in K-Group

## Problem
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as they are.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

## My Approach

I realized this problem requires:
1. Pre-calculating the total length to identify incomplete groups
2. Reversing nodes k at a time while tracking group boundaries
3. Connecting each reversed group's new head to the previous group's tail
4. Leaving incomplete groups unchanged

The key insight is that after reversing a group, its original head becomes its tail, which needs to connect to the next group.

## Solution with Clean Variable Names and Comments

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Step 1: Count total nodes to identify incomplete groups
        total_nodes = 0
        temp = head
        while temp:
            total_nodes += 1
            temp = temp.next
        
        # Calculate how many nodes belong to complete groups
        nodes_to_reverse = (total_nodes // k) * k
        
        # Initialize pointers for reversal
        current = head
        previous = None
        nodes_processed = 0
        
        # Dummy node to simplify head management
        dummy = ListNode(0)
        previous_group_tail = dummy
        current_group_tail = head  # First node becomes tail after reversal
        
        while current:
            # Stop reversing when we reach the incomplete group
            if nodes_processed == nodes_to_reverse:
                # Connect incomplete group as-is
                previous_group_tail.next = current
                break
            
            # Reverse current node
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
            nodes_processed += 1
            
            # Check if we completed a group of k nodes
            if nodes_processed % k == 0:
                # Connect previous group's tail to current group's new head
                # 'previous' is now the head of the reversed group
                previous_group_tail.next = previous
                
                # Update tail pointer for next group connection
                # The original head of this group is now its tail
                previous_group_tail = current_group_tail
                
                # Reset for next group
                current_group_tail = current  # Next node will be new group's tail
                previous = None
        
        return dummy.next
```

## Visual Intuition

### Example: k = 3, list = [1,2,3,4,5,6,7,8]

```
Initial: 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8
         └─Group 1─┘ └─Group 2─┘ └Incomplete┘

Step-by-step reversal of Group 1:

Start Group 1:
current_group_tail = 1 (will be tail after reversal)
1 → 2 → 3 → 4 → 5 → 6 → 7 → 8
↑
current

After reversing 1:
None ← 1   2 → 3 → 4 → 5 → 6 → 7 → 8
       ↑   ↑
    previous current

After reversing 2:
None ← 1 ← 2   3 → 4 → 5 → 6 → 7 → 8
           ↑   ↑
        previous current

After reversing 3 (group complete):
None ← 1 ← 2 ← 3   4 → 5 → 6 → 7 → 8
               ↑   ↑
            previous current

Connect to result:
dummy → 3 → 2 → 1   4 → 5 → 6 → 7 → 8
                ↑   ↑
                |   current (start of next group)
                └── previous_group_tail updated to here

Continue with Group 2:
current_group_tail = 4 (will be tail after reversal)

After reversing Group 2:
dummy → 3 → 2 → 1 → 6 → 5 → 4   7 → 8
                              ↑   ↑
                              |   current
                              └── previous_group_tail

Check: nodes_processed = 6 = nodes_to_reverse
Attach incomplete group:
dummy → 3 → 2 → 1 → 6 → 5 → 4 → 7 → 8

Final: 3 → 2 → 1 → 6 → 5 → 4 → 7 → 8
```

### Detailed Pointer Movement

```
For k=2, list=[1,2,3,4,5]:

Initial state:
dummy → None
previous_group_tail = dummy
current_group_tail = 1
current = 1

After reversing first group [1,2]:
Nodes:    dummy → 2 → 1 → 3 → 4 → 5
Pointers: previous_group_tail = 1
          current_group_tail = 3
          current = 3

After reversing second group [3,4]:
Nodes:    dummy → 2 → 1 → 4 → 3 → 5
Pointers: previous_group_tail = 3
          current = 5

Node 5 is incomplete group (< k), attach as-is:
Final:    dummy → 2 → 1 → 4 → 3 → 5
```

## Why This Works

The algorithm maintains several key invariants:
1. **Group boundary tracking**: We know exactly when a group of k nodes is complete
2. **Tail preservation**: The first node of each group becomes its tail after reversal
3. **Connection management**: Each group's tail connects to the next group's head
4. **Incomplete group handling**: Pre-calculation ensures we stop reversing at the right point

## Complexity Analysis

### Time Complexity: O(n)
- First pass to count nodes: O(n)
- Second pass to reverse: O(n)
- Each node is visited at most twice
- Total: O(2n) = O(n)

### Space Complexity: O(1)
- Only using a constant number of pointers
- In-place reversal without extra data structures

## Edge Cases

```python
# Edge Case 1: k equals list length
head = [1,2,3,4], k = 4
# Result: [4,3,2,1] - entire list reversed

# Edge Case 2: k = 1 (no reversal needed)
head = [1,2,3,4], k = 1
# Result: [1,2,3,4] - unchanged

# Edge Case 3: k > list length
head = [1,2], k = 3
# Result: [1,2] - no complete groups, unchanged

# Edge Case 4: Single node
head = [1], k = 2
# Result: [1] - incomplete group

# Edge Case 5: Perfect multiple of k
head = [1,2,3,4,5,6], k = 2
# Result: [2,1,4,3,6,5] - all groups complete

# Edge Case 6: One complete group + incomplete
head = [1,2,3,4,5], k = 3
# Result: [3,2,1,4,5] - first group reversed, second unchanged
```

## Key Insights

1. **Pre-calculation is crucial** - Knowing total length prevents reversing incomplete groups

2. **Group boundary management** - The modulo operator (`%`) elegantly identifies group completion

3. **Pointer role switching** - The head of each group becomes its tail after reversal

4. **Dummy node pattern** - Simplifies handling the new head of the entire list

5. **In-place reversal** - Standard reversal technique applied with group awareness

## Common Mistakes

1. **Reversing incomplete groups**:
   ```python
   # Wrong: Reverses all nodes including incomplete group
   while current:
       # reversal logic
   
   # Correct: Check if we've reached incomplete group
   if nodes_processed == nodes_to_reverse:
       previous_group_tail.next = current
       break
   ```

2. **Losing group connections**:
   ```python
   # Wrong: Forgetting to connect groups
   if nodes_processed % k == 0:
       # Missing connection logic
   
   # Correct: Connect previous tail to new head
   previous_group_tail.next = previous
   ```

3. **Incorrect tail tracking**:
   ```python
   # Wrong: Not saving the original head (future tail)
   # The first node becomes the tail after reversal!
   
   # Correct: Save it before reversal starts
   current_group_tail = current  # or head for first group
   ```

4. **Off-by-one in counting**:
   ```python
   # Wrong: Checking before incrementing
   if nodes_processed % k == 0:
   nodes_processed += 1
   
   # Correct: Increment first, then check
   nodes_processed += 1
   if nodes_processed % k == 0:
   ```

## Alternative Approach - Recursive

```python
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Check if we have k nodes to reverse
        current = head
        for _ in range(k):
            if not current:
                return head  # Less than k nodes, return as-is
            current = current.next
        
        # Reverse k nodes
        prev = self.reverseKGroup(current, k)  # Recursively process rest
        current = head
        
        for _ in range(k):
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        return prev
```

While elegant, the recursive approach uses O(n/k) stack space.

## Pattern Recognition

This problem demonstrates:
- **Group-wise processing** - Operating on fixed-size chunks
- **In-place list manipulation** - Modifying structure without extra space
- **Boundary management** - Handling complete vs incomplete groups

Similar problems:
- Reverse Linked List (k = entire length)
- Reverse Linked List II (reverse between positions)
- Swap Nodes in Pairs (k = 2 special case)
- Rotate List (different transformation)

## What I Learned

The key challenge was managing multiple pointer relationships: tracking the current reversal, group boundaries, and inter-group connections. Pre-calculating the total length was crucial to handle incomplete groups correctly. The insight that the first node of each group becomes its tail after reversal helped me understand the connection logic. This problem beautifully combines basic linked list reversal with careful boundary management - a pattern that appears in many real-world scenarios like packet processing or batch operations.