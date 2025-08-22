# Copy Linked List with Random Pointer

## Problem
A linked list of length `n` is given such that each node contains an additional random pointer, which could point to any node in the list, or `null`.

Construct a deep copy of the list. The deep copy should consist of exactly `n` brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the `next` and `random` pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state.

Return the head of the copied linked list.

## My Approach

I used a hash map to maintain the mapping between original nodes and their copies. This allows me to create all nodes first, then connect the pointers in a second pass without worrying about forward references.

## Solution with Comments

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # HashMap to store mapping from original node to copied node
        # This allows us to find the copy of any node in O(1) time
        hash_map = {}
        
        # Dummy node to simplify building the new list
        new_head = Node(-1)
        
        # First pass: Create all new nodes and store in hash map
        # We only set values here, not pointers
        curr = head
        while curr:
            # Create a new node with the same value
            new_node = Node(curr.val)
            # Map original node to its copy
            hash_map[curr] = new_node
            
            # Connect the first node to dummy
            # (This just helps us track the head of new list)
            if new_head.next is None:
                new_head.next = new_node
            
            curr = curr.next
        
        # Second pass: Connect all next and random pointers
        # Now that all nodes exist, we can set any pointer
        for orig_node, new_node in hash_map.items():
            # Set next pointer: map original's next to new node's next
            if orig_node.next is not None:
                new_node.next = hash_map[orig_node.next]
            else:
                new_node.next = None
            
            # Set random pointer: map original's random to new node's random
            if orig_node.random is not None:
                new_node.random = hash_map[orig_node.random]
            else:
                new_node.random = None
        
        # Return the head of the copied list (skip dummy)
        return new_head.next
```

## Visual Intuition

```
Original List Example:

Nodes with next pointers:
Node(7) ──next──> Node(13) ──next──> Node(11) ──next──> None

Random pointer connections:
- Node(7).random  = None
- Node(13).random = Node(7)   (points back to first node)
- Node(11).random = Node(13)  (points back to second node)

Visual representation:
        ┌──────────────┐
        ↓              │
[7] → [13] → [11] → None
 ↓      ↑──────┘
None    

Or in a clearer format:
Position:    0         1          2
           [7]  →   [13]  →    [11]  → None
            ↓        ↓          ↓
         random:   random:    random:
           None    pos 0      pos 1

Step 1 - Create all new nodes:
Original nodes: [7], [13], [11]
New nodes:      [7'], [13'], [11']

Build hash_map:
{
    Node(7):  Node'(7),
    Node(13): Node'(13),
    Node(11): Node'(11)
}

Step 2 - Connect pointers using hash map:

For each original node and its copy:
- Node(7) → Node'(7):
  - next: Node'(7).next = Node'(13)  (from hash_map[Node(13)])
  - random: Node'(7).random = None
  
- Node(13) → Node'(13):
  - next: Node'(13).next = Node'(11)  (from hash_map[Node(11)])
  - random: Node'(13).random = Node'(7)  (from hash_map[Node(7)])
  
- Node(11) → Node'(11):
  - next: Node'(11).next = None
  - random: Node'(11).random = Node'(13)  (from hash_map[Node(13)])

Result - Deep Copied List:
Position:    0         1          2
           [7']  →   [13']  →   [11']  → None
            ↓         ↓          ↓
         random:    random:    random:
           None     pos 0      pos 1

The structure is identical but with completely new nodes!
```

## Alternative: O(1) Space Interweaving Approach

This clever approach avoids the hash map by interweaving copied nodes with originals:

```python
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        # Step 1: Create copied nodes and interweave with original
        # A → A' → B → B' → C → C'
        curr = head
        while curr:
            copied = Node(curr.val, curr.next)
            curr.next = copied
            curr = copied.next
        
        # Step 2: Set random pointers for copied nodes
        # Use the fact that copied node is always after original
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        
        # Step 3: Separate the two lists
        dummy = Node(0)
        copy_prev = dummy
        curr = head
        
        while curr:
            copy = curr.next
            curr.next = copy.next
            copy_prev.next = copy
            
            copy_prev = copy
            curr = curr.next
        
        return dummy.next
```

## Complexity Analysis

### Hash Map Approach (My Solution)
- **Time Complexity:** O(n)
  - First pass to create nodes: O(n)
  - Second pass to connect pointers: O(n)
  - Total: O(2n) = O(n)
- **Space Complexity:** O(n)
  - Hash map storing n node mappings

### Interweaving Approach
- **Time Complexity:** O(n)
  - Three passes, each O(n)
- **Space Complexity:** O(1)
  - No extra data structures (only the output list)

## Edge Cases

```python
# Edge Case 1: Empty list
head = None
# Returns: None

# Edge Case 2: Single node with no random
head = Node(1)
# Returns: Node(1) with no connections

# Edge Case 3: Single node with self-random
head = Node(1)
head.random = head
# Returns: Node(1) with random pointing to itself

# Edge Case 4: Circular next pointers
# The hash map approach handles this naturally

# Edge Case 5: All randoms point to one node
# Again, hash map handles this correctly
```

## Key Insights

1. **Hash map for node mapping** - The key insight is maintaining a mapping from original to copied nodes, enabling O(1) lookup

2. **Two-pass approach** - Creating all nodes first avoids forward reference issues when setting pointers

3. **Null checking** - Both next and random can be null, requiring careful checking

4. **Deep vs shallow copy** - We create entirely new nodes, not just copying pointers

## Common Mistakes

1. **Setting pointers during node creation**:
   ```python
   # Wrong: Random might point to node not yet created
   new_node.random = orig_node.random  # Points to original!
   
   # Correct: Map through hash map
   new_node.random = hash_map[orig_node.random]
   ```

2. **Forgetting null checks**:
   ```python
   # Wrong: Crashes if random is None
   new_node.random = hash_map[orig_node.random]
   
   # Correct:
   if orig_node.random:
       new_node.random = hash_map[orig_node.random]
   ```

3. **Modifying original list**:
   ```python
   # Wrong: The interweaving approach temporarily modifies original
   # Make sure to restore it!
   ```

## Pattern Recognition

This problem demonstrates:
- **Hash map for graph cloning** - Similar pattern for copying any graph structure
- **Two-pass construction** - Create nodes, then connect
- **Space-time tradeoff** - Hash map uses O(n) space for simplicity

Similar problems:
- Clone Graph (same concept, different structure)
- Copy List with Random Pointer II
- Deep copy of tree with parent pointers

## What I Learned

The hash map approach is intuitive and clean - it directly models the relationship between original and copied nodes. While the interweaving approach is clever and saves space, the hash map solution is more maintainable and extends naturally to other graph copying problems. The key insight is that we need a way to map from original nodes to their copies, and a hash map is the most straightforward way to achieve this.