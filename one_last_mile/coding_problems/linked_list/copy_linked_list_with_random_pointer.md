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

## Alternative 1: Index-Based Approach (My Creative Solution)

This approach uses the original nodes' values as temporary storage for indices, creating an implicit mapping without a hash map:

```python
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
            
        temp = head
        results = []  # List to store new nodes

        # Phase 1: Create copy nodes and store original values as indices
        idx = 0
        while temp:
            # Create new node with original value
            results.append(Node(temp.val, None, temp.random))
            # Temporarily store index in original node's value
            temp.val = idx
            idx += 1
            temp = temp.next

        # Phase 2: Connect next pointers in the new list
        for idx in range(len(results)-1):
            results[idx].next = results[idx+1]

        # Phase 3: Fix random pointers using the index mapping
        # node.random still points to original nodes, which now have indices as values
        for node in results:
            if node.random:
                # Use the index stored in original node to find corresponding new node
                node.random = results[node.random.val]
            else:
                node.random = None

        # Get the head of new list
        new_head = results[0]

        # Phase 4: Restore original values in the original list
        temp1, temp2 = head, new_head
        while temp1 and temp2:
            temp1.val = temp2.val  # Restore from copy
            temp1 = temp1.next
            temp2 = temp2.next

        return new_head
```

### Visual Example of Index-Based Approach:

```
Original: [7] → [13] → [11]
           ↓     ↓      ↓
        random: None   [7]   [13]

Step 1 - Replace values with indices:
Original: [0] → [1] → [2]  (values replaced with indices)
           ↓     ↓     ↓
        random: None  [0]   [1]

Create:  results = [Node(7), Node(13), Node(11)]

Step 2 - Connect next pointers:
results: [7] → [13] → [11] → None

Step 3 - Fix random pointers:
- results[0].random = None (was None)
- results[1].random = results[0] (using index 0 from original)
- results[2].random = results[1] (using index 1 from original)

Step 4 - Restore original values:
Original: [7] → [13] → [11] (values restored)
```

### Complexity Analysis:
- **Time:** O(n) - Four passes through the list
- **Space:** O(n) - The list container is auxiliary space
- **Key Insight:** Uses original list as implicit index mapping

## Alternative 2: O(1) Space Interweaving Approach

This approach avoids both hash map and list by interweaving copied nodes with originals:

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

### Hash Map Approach (First Solution)
- **Time Complexity:** O(n)
  - First pass to create nodes: O(n)
  - Second pass to connect pointers: O(n)
  - Total: O(2n) = O(n)
- **Space Complexity:** O(n)
  - Hash map storing n node mappings

### Index-Based Approach (Creative Solution)
- **Time Complexity:** O(n)
  - Phase 1: Create nodes and modify values: O(n)
  - Phase 2: Connect next pointers: O(n)
  - Phase 3: Fix random pointers: O(n)
  - Phase 4: Restore original values: O(n)
  - Total: O(4n) = O(n)
- **Space Complexity:** O(n)
  - Python list container for nodes (auxiliary space)
  - Note: The nodes themselves are required output, but the list container is extra
- **Modifies Input:** Yes (temporarily changes values, then restores)

### Interweaving Approach (True O(1) Space)
- **Time Complexity:** O(n)
  - Three passes, each O(n)
- **Space Complexity:** O(1)
  - No extra data structures (only the output list)
- **Modifies Input:** Yes (temporarily changes structure, then restores)

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

## Comparison of All Three Approaches

| Approach | Time | Auxiliary Space | Modifies Input | Key Technique |
|----------|------|-----------------|----------------|---------------|
| Hash Map | O(n) | O(n) - hash map | No | Explicit node mapping |
| Index-Based | O(n) | O(n) - list container | Yes (restored) | Values as indices |
| Interweaving | O(n) | O(1) | Yes (restored) | Pointer manipulation |

### When to Use Each:
- **Hash Map**: Most intuitive, doesn't modify input, standard approach
- **Index-Based**: Creative when you can modify values temporarily
- **Interweaving**: When true O(1) auxiliary space is required

## What I Learned

The hash map approach is intuitive and clean - it directly models the relationship between original and copied nodes. My index-based solution shows that we can use the original list itself as implicit storage by temporarily repurposing node values as indices - essentially creating an in-place hash map! While the interweaving approach achieves true O(1) auxiliary space, all three solutions demonstrate different ways to solve the fundamental problem: maintaining a mapping between original and copied nodes.

The key insight across all approaches is that we need a way to map from original nodes to their copies:
- Hash map does this explicitly
- Index-based uses the original list as the mapping
- Interweaving uses pointer structure as the mapping