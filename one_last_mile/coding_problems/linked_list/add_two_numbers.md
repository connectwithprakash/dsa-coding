# Add Two Numbers

## Problem
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

## My Approach

I realized I could save space by reusing one of the input lists as the result. By counting the lengths first and ensuring I use the longer list, I avoid creating new nodes except for a potential final carry.

## Solution - In-Place Modification

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Step 1: Count the length of both lists
        n1, n2 = 0, 0
        
        l1_curr = l1
        while l1_curr:
            n1 += 1
            l1_curr = l1_curr.next
        
        l2_curr = l2
        while l2_curr:
            n2 += 1
            l2_curr = l2_curr.next
        
        # Step 2: Ensure l1 is the longer list (we'll modify it)
        if n1 < n2:
            l1, l2 = l2, l1
        
        # Step 3: Add digits and store result in l1
        l1_curr = l1  # Current position in longer list
        l2_curr = l2  # Current position in shorter list
        carry = 0
        prev = None   # Track last node for potential carry
        
        while l1_curr:
            # Calculate sum at current position
            sum_ = l1_curr.val + carry
            if l2_curr:
                sum_ += l2_curr.val
                l2_curr = l2_curr.next
            
            # Update digit and carry
            ones = sum_ % 10
            carry = sum_ // 10
            l1_curr.val = ones  # Modify in place
            
            # Move to next position
            prev = l1_curr
            l1_curr = l1_curr.next
        
        # Step 4: Handle final carry if present
        if carry > 0:
            prev.next = ListNode(carry)
        
        return l1  # Return modified longer list
```

## Standard Solution - Create New List

```python
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        carry = 0
        
        # Process both lists simultaneously
        while l1 or l2 or carry:
            # Get values (0 if node doesn't exist)
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate sum and carry
            total = val1 + val2 + carry
            carry = total // 10
            
            # Create new node with digit
            current.next = ListNode(total % 10)
            current = current.next
            
            # Move to next nodes
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next
```

## Visual Intuition

```
Example: 342 + 465 = 807
(Stored as 2→4→3 and 5→6→4)

My In-Place Approach:
Step 1: Count lengths
l1: 2→4→3 (length = 3)
l2: 5→6→4 (length = 3)
Same length, no swap needed

Step 2: Add with carry
Position 1: 2 + 5 = 7, carry = 0
            l1: 7→4→3
            
Position 2: 4 + 6 + 0 = 10, carry = 1
            l1: 7→0→3
            
Position 3: 3 + 4 + 1 = 8, carry = 0
            l1: 7→0→8

Result: 7→0→8 (represents 807)

Example with different lengths:
l1: 9→9 (99)
l2: 1   (1)
Sum: 100

After length check and swap:
l1: 9→9 (longer)
l2: 1   (shorter)

Addition:
Position 1: 9 + 1 = 10 → digit=0, carry=1
            l1: 0→9
Position 2: 9 + 0 + 1 = 10 → digit=0, carry=1
            l1: 0→0
Final carry: Create new node(1)
            l1: 0→0→1

Result: 0→0→1 (represents 100)
```

## Complexity Analysis

### My In-Place Solution
- **Time Complexity:** O(max(m, n))
  - Count lengths: O(m) + O(n)
  - Addition: O(max(m, n))
  - Total: O(max(m, n))
- **Space Complexity:** O(1)
  - Only creating at most one new node for carry
  - Reusing existing nodes for result

### Standard Solution
- **Time Complexity:** O(max(m, n))
  - Single pass through both lists
- **Space Complexity:** O(max(m, n))
  - Creating new list with max(m, n) + 1 nodes

## Edge Cases

```python
# Edge Case 1: Different lengths
l1: 1→2→3 (321)
l2: 4→5   (54)
Result: 5→7→3 (375)

# Edge Case 2: Final carry
l1: 9→9→9 (999)
l2: 1     (1)
Result: 0→0→0→1 (1000)

# Edge Case 3: One list is just 0
l1: 0
l2: 3→4→5
Result: 3→4→5

# Edge Case 4: Both single digits with carry
l1: 5
l2: 5
Result: 0→1 (10)
```

## Key Insights

1. **Reverse order simplifies addition** - We naturally process from least significant digit, just like manual addition

2. **In-place modification saves space** - By reusing the longer list, we minimize new node creation

3. **Length counting trade-off** - Extra O(m+n) time for counting saves O(max(m,n)) space

4. **Carry propagation** - The carry can at most be 1 (since max digit sum is 9+9+1=19)

## Common Mistakes

1. **Forgetting final carry**:
   ```python
   # Wrong: Not handling carry after loop
   while l1_curr:
       # addition logic
   # Missing: if carry > 0: create new node
   ```

2. **Not handling different lengths**:
   ```python
   # Wrong: Assuming both lists same length
   while l1 and l2:  # Stops when shorter list ends
   ```

3. **Modifying without checking which is longer**:
   ```python
   # Wrong: Might run out of nodes
   # Need to ensure we're modifying the longer list
   ```

## Pattern Recognition

This problem demonstrates:
- **Digit-by-digit processing** - Similar to string/array addition problems
- **Carry propagation** - Classic in arithmetic operations
- **In-place modification** - Space optimization technique

Similar problems:
- Add Two Numbers II (not reversed)
- Multiply Strings
- Plus One (array version)
- Add Binary

## What I Learned

The key insight was recognizing that the reverse order actually simplifies the problem - we don't need to reverse anything! My approach of reusing the longer list shows that sometimes we can optimize space by modifying input (when allowed). The standard approach with a dummy node is cleaner but uses more space. This problem beautifully combines linked list manipulation with basic arithmetic operations.