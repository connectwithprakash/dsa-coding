# Invert Binary Tree

## Problem
Given the root of a binary tree, invert the tree, and return its root.

## My Approach

I realized that inverting a tree means swapping left and right children at every node. Using recursion, I can invert each subtree first, then swap the children at the current node. This is a post-order traversal approach.

## Solution

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base case: empty tree
        if root is None:
            return
        
        # Recursively invert left subtree
        if root.left:
            self.invertTree(root.left)
        
        # Recursively invert right subtree
        if root.right:
            self.invertTree(root.right)
        
        # Swap the children at current node
        root.left, root.right = root.right, root.left
        
        return root
```

## Alternative Solution - Cleaner Version

```python
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        # Swap children first (pre-order approach)
        root.left, root.right = root.right, root.left
        
        # Then recursively invert subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root
```

## Visual Intuition

### Example Tree Inversion

```
Original Tree:
        4
       / \
      2   7
     / \ / \
    1  3 6  9

Step-by-step (Post-order approach):
1. Reach leaf nodes (1, 3, 6, 9) - nothing to swap
2. At node 2: swap children 1 and 3
3. At node 7: swap children 6 and 9
4. At root 4: swap children 2 and 7

Inverted Tree:
        4
       / \
      7   2
     / \ / \
    9  6 3  1
```

### Recursion Flow Visualization

```
invertTree(4)
├── invertTree(2)
│   ├── invertTree(1) → returns 1
│   ├── invertTree(3) → returns 3
│   └── swap: 2.left=3, 2.right=1
├── invertTree(7)
│   ├── invertTree(6) → returns 6
│   ├── invertTree(9) → returns 9
│   └── swap: 7.left=9, 7.right=6
└── swap: 4.left=7, 4.right=2
```

## Why Both Approaches Work

### My Post-Order Approach
- **Process children first, then swap**
- Inverts from bottom to top
- Natural recursive thinking: "invert everything below, then swap"

### Pre-Order Alternative
- **Swap first, then process children**
- Inverts from top to bottom
- Simpler code: swap happens before recursive calls

Both work because:
1. Every node's children get swapped exactly once
2. The order doesn't matter - we're just rearranging pointers
3. Each subtree becomes properly inverted

## Iterative Solution Using Queue (BFS)

```python
from collections import deque

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        queue = deque([root])
        
        while queue:
            node = queue.popleft()
            
            # Swap children
            node.left, node.right = node.right, node.left
            
            # Add children to queue for processing
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return root
```

## Complexity Analysis

### Recursive Solutions
- **Time Complexity:** O(n)
  - Visit every node exactly once
  - Swap operation is O(1)
- **Space Complexity:** O(h)
  - Recursion stack depth equals tree height
  - Best case (balanced): O(log n)
  - Worst case (skewed): O(n)

### Iterative Solution
- **Time Complexity:** O(n)
  - Process every node once
- **Space Complexity:** O(w)
  - Queue holds at most one level
  - w = maximum width of tree
  - Worst case: O(n/2) for complete tree

## Edge Cases

```python
# Edge Case 1: Empty tree
root = None
# Result: None

# Edge Case 2: Single node
root = TreeNode(1)
# Result: TreeNode(1) - unchanged

# Edge Case 3: Only left child
#     1
#    /
#   2
# Result:
#     1
#      \
#       2

# Edge Case 4: Skewed tree (linked list-like)
#     1
#      \
#       2
#        \
#         3
# Result:
#     1
#    /
#   2
#  /
# 3
```

## Key Insights

1. **Recursion naturally handles trees** - The tree structure mirrors the recursive call structure

2. **Post-order vs Pre-order** - Both work for inversion; choice depends on preference

3. **In-place modification** - We're rearranging pointers, not creating new nodes

4. **Symmetry of the problem** - Inverting twice returns the original tree

5. **The None checks in my solution are redundant** - The base case handles None, so checking before recursion isn't necessary

## Common Mistakes

1. **Forgetting to return root**:
   ```python
   # Wrong: No return statement
   def invertTree(self, root):
       if root is None:
           return  # Missing root here
       # ...operations...
       # Missing: return root
   ```

2. **Creating new nodes instead of swapping**:
   ```python
   # Wrong: Creating new tree
   new_root = TreeNode(root.val)
   new_root.left = self.invertTree(root.right)
   
   # Correct: Swap in place
   root.left, root.right = root.right, root.left
   ```

3. **Incorrect swap syntax**:
   ```python
   # Wrong: This doesn't swap!
   root.left = root.right
   root.right = root.left  # Now both point to same node
   
   # Correct: Simultaneous assignment
   root.left, root.right = root.right, root.left
   ```

## Pattern Recognition

This problem demonstrates:
- **Tree traversal** - Can be solved with any traversal order
- **Recursive tree manipulation** - Modifying structure while traversing
- **Pointer manipulation** - Swapping references

Similar problems:
- Symmetric Tree (check if tree is mirror of itself)
- Maximum Depth of Binary Tree (tree traversal)
- Same Tree (comparing tree structures)
- Flatten Binary Tree to Linked List (tree restructuring)

## What I Learned

The elegance of tree recursion really shines here - the solution is almost trivial once you understand that you just need to swap children at each node. My initial approach with the redundant None checks shows I was being overly cautious. The problem teaches that sometimes the simplest approach (swap and recurse) is the best. It's also interesting that pre-order, post-order, and even level-order (BFS) all work - the key operation is the swap, not the traversal order.