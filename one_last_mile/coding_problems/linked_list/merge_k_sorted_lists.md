# Merge K Sorted Lists

## Problem
You are given an array of `k` linked lists `lists`, each linked list is sorted in ascending order.

Merge all the linked lists into one sorted linked list and return it.

## My Approach

I realized I can repeatedly find the minimum value among all list heads and add it to the result. By tracking which list has the minimum, I can advance that list's pointer and continue until all lists are exhausted. This gives me O(n*k) time with O(1) space.

## Solution with Improved Names and Comments

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Dummy head eliminates edge case of empty result
        dummy_head = ListNode(0)
        current = dummy_head
        
        # Keep merging until all lists are exhausted
        while True:
            # Track the minimum value and which list it came from
            min_value = float("inf")
            min_list_index = -1  # -1 indicates no valid list found
            
            # Linear scan through all k lists to find global minimum
            # This is the key operation that gives us O(k) per node
            for list_index in range(len(lists)):
                # Check if this list has remaining nodes
                if lists[list_index] and (lists[list_index].val < min_value):
                    min_value = lists[list_index].val
                    min_list_index = list_index
            
            # If we found a minimum, add it to our merged result
            if min_list_index > -1:
                # Attach the minimum node to our result
                current.next = lists[min_list_index]
                current = current.next
                
                # Advance the pointer in the list we took from
                # This "consumes" the node from that list
                lists[min_list_index] = lists[min_list_index].next
            else:
                # No valid list found means all lists are exhausted
                break

        return dummy_head.next
```

## Visual Intuition

### Example: Merging 3 Lists

```
Initial State:
lists[0]: 1 → 4 → 5
lists[1]: 1 → 3 → 4
lists[2]: 2 → 6

Result: dummy → 

Step 1: Find minimum among [1, 1, 2]
        Choose lists[0] (could also choose lists[1])
lists[0]: 4 → 5      (advanced)
lists[1]: 1 → 3 → 4
lists[2]: 2 → 6
Result: dummy → 1 →

Step 2: Find minimum among [4, 1, 2]
        Choose lists[1]
lists[0]: 4 → 5
lists[1]: 3 → 4      (advanced)
lists[2]: 2 → 6
Result: dummy → 1 → 1 →

Step 3: Find minimum among [4, 3, 2]
        Choose lists[2]
lists[0]: 4 → 5
lists[1]: 3 → 4
lists[2]: 6          (advanced)
Result: dummy → 1 → 1 → 2 →

Step 4: Find minimum among [4, 3, 6]
        Choose lists[1]
lists[0]: 4 → 5
lists[1]: 4          (advanced)
lists[2]: 6
Result: dummy → 1 → 1 → 2 → 3 →

Step 5: Find minimum among [4, 4, 6]
        Choose lists[0]
lists[0]: 5          (advanced)
lists[1]: 4
lists[2]: 6
Result: dummy → 1 → 1 → 2 → 3 → 4 →

Step 6: Find minimum among [5, 4, 6]
        Choose lists[1]
lists[0]: 5
lists[1]: None       (exhausted)
lists[2]: 6
Result: dummy → 1 → 1 → 2 → 3 → 4 → 4 →

Step 7: Find minimum among [5, None, 6]
        Choose lists[0]
lists[0]: None       (exhausted)
lists[1]: None
lists[2]: 6
Result: dummy → 1 → 1 → 2 → 3 → 4 → 4 → 5 →

Step 8: Find minimum among [None, None, 6]
        Choose lists[2]
lists[0]: None
lists[1]: None
lists[2]: None       (exhausted)
Result: dummy → 1 → 1 → 2 → 3 → 4 → 4 → 5 → 6 →

Step 9: All lists exhausted, return result
Final: 1 → 1 → 2 → 3 → 4 → 4 → 5 → 6
```

### Algorithm Visualization

```
For each node to be added:
┌─────────────────────────────────┐
│  Scan all k list heads: O(k)    │
│  ┌───┬───┬───┬───┬───┬───┐     │
│  │ 3 │ 1 │ 7 │ 2 │ 5 │ 4 │     │
│  └───┴───┴───┴───┴───┴───┘     │
│        ↑                         │
│    minimum = 1                   │
└─────────────────────────────────┘
                ↓
    Add to result and advance
```

## Complexity Analysis

### Time Complexity: O(n * k)
- We process n total nodes
- For each node, we scan k lists to find the minimum
- Total: n iterations × k comparisons = O(n * k)

### Space Complexity: O(1)
- We only use a few variables (dummy_head, current, min_value, min_list_index)
- We reuse existing nodes, not creating new ones
- The lists array is given as input, not extra space

## Alternative Approaches

### 1. Min-Heap Approach - O(n * log k) time, O(k) space

```python
import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Min-heap to always get the smallest element in O(log k)
        heap = []
        
        # Initialize heap with first node of each list
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
        
        dummy_head = ListNode(0)
        current = dummy_head
        
        while heap:
            # Extract minimum in O(log k)
            val, list_idx, node = heapq.heappop(heap)
            current.next = node
            current = current.next
            
            # Add next node from same list if exists
            if node.next:
                heapq.heappush(heap, (node.next.val, list_idx, node.next))
        
        return dummy_head.next
```

### 2. Divide and Conquer - O(n * log k) time, O(1) space

```python
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        # Repeatedly merge pairs until one list remains
        while len(lists) > 1:
            merged_lists = []
            
            # Merge lists in pairs
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                merged_lists.append(self.merge2Lists(l1, l2))
            
            lists = merged_lists
        
        return lists[0]
    
    def merge2Lists(self, l1, l2):
        dummy = ListNode(0)
        current = dummy
        
        while l1 and l2:
            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        
        current.next = l1 or l2
        return dummy.next
```

## Approach Comparison

| Approach | Time Complexity | Space Complexity | Pros | Cons |
|----------|----------------|------------------|------|------|
| **Linear Scan (My Solution)** | O(n*k) | O(1) | Simple, optimal space | Slower for large k |
| Min-Heap | O(n*log k) | O(k) | Faster for large k | Extra space for heap |
| Divide & Conquer | O(n*log k) | O(1) | Fast and space-efficient | More complex code |

My solution is optimal when:
- k is small (the O(k) scan is negligible)
- Space is critical (true O(1) space)
- Simplicity is valued

## Edge Cases

```python
# Edge Case 1: Empty input
lists = []
# Result: None

# Edge Case 2: Single list
lists = [[1,2,3]]
# Result: [1,2,3]

# Edge Case 3: Some empty lists
lists = [[], [1,2], [], [3,4]]
# Result: [1,2,3,4]

# Edge Case 4: All empty lists
lists = [[], [], []]
# Result: None

# Edge Case 5: Lists with duplicate values
lists = [[1,1,2], [1,2,3]]
# Result: [1,1,1,2,2,3]

# Edge Case 6: Single node lists
lists = [[1], [2], [3]]
# Result: [1,2,3]
```

## Key Insights

1. **Linear scan is valid** - While O(n*k) seems worse than O(n*log k), it's still polynomial and meets the stated requirement

2. **Space matters** - My O(1) space is truly constant, while heap uses O(k) which could be significant

3. **Node reuse** - We're moving existing nodes, not creating new ones, which is memory efficient

4. **Sentinel value pattern** - Using -1 for "no list found" avoids complex boolean checks

5. **Dummy head pattern** - Eliminates edge case of building the first node

## Common Mistakes

1. **Creating new nodes instead of reusing**:
   ```python
   # Wrong: Creating new nodes wastes memory
   current.next = ListNode(lists[min_list_index].val)
   
   # Correct: Reuse existing nodes
   current.next = lists[min_list_index]
   ```

2. **Not handling empty lists**:
   ```python
   # Wrong: Assumes all lists are non-empty
   if lists[list_index].val < min_value:
   
   # Correct: Check for null first
   if lists[list_index] and lists[list_index].val < min_value:
   ```

3. **Incorrect termination condition**:
   ```python
   # Wrong: Only checks if lists array is empty
   while lists:
   
   # Correct: Check if any list has nodes
   while any(lst for lst in lists):
   # Or use the min_list_index sentinel approach
   ```

4. **Not advancing the chosen list**:
   ```python
   # Wrong: Infinite loop on same minimum
   current.next = lists[min_list_index]
   # Missing: lists[min_list_index] = lists[min_list_index].next
   ```

## Pattern Recognition

This problem demonstrates:
- **K-way merge** - Fundamental pattern in external sorting, database joins
- **Priority queue alternative** - Linear scan vs heap tradeoff
- **Dummy node pattern** - Simplifying list construction

Similar problems:
- Merge Two Sorted Lists (k=2 special case)
- Find K Pairs with Smallest Sums
- Smallest Range Covering Elements from K Lists
- Merge Sorted Array (array version)

## What I Learned

The key insight is that "better than O(n*k)" doesn't always mean we need the absolute best time complexity. My O(n*k) solution with O(1) space is perfectly valid and arguably superior to the O(n*log k) heap solution that uses O(k) space. The linear scan approach is beautifully simple - just repeatedly find the minimum and advance. Sometimes the straightforward solution is the best, especially when k is small or space is at a premium.