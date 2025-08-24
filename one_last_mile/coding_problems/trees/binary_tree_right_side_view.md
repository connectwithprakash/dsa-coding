# Binary Tree Right Side View

## Problem
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

## My Approach

I realized that the right side view is simply the last node at each level. By reusing level order traversal and taking the last element from each level, I get the rightmost visible node. If a level only has left children, they become visible from the right.

## Solution with Comments

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Get level order traversal
        all_levels = self.levelOrder(root)
        # Extract last element from each level (rightmost node)
        return [level[-1] for level in all_levels]

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.levels_result = []
        
        def traverse_by_level(current_node, depth):
            # Check if we need to create a new level
            if len(self.levels_result) == depth:
                self.levels_result.append([])
            
            # Add current node's value to its level
            self.levels_result[depth].append(current_node.val)
            
            # Traverse left subtree first (maintains left-to-right order)
            if current_node.left:
                traverse_by_level(current_node.left, depth + 1)
            # Then traverse right subtree
            if current_node.right:
                traverse_by_level(current_node.right, depth + 1)
        
        if root:
            traverse_by_level(root, 0)  # Start at depth 0
        
        return self.levels_result
```

## Optimized Solution - Direct Collection

```python
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        right_view = []
        
        def dfs(node, depth):
            # First node we see at this depth is the rightmost
            # (because we traverse right subtree first)
            if depth == len(right_view):
                right_view.append(node.val)
            
            # Visit right first to ensure rightmost is seen first
            if node.right:
                dfs(node.right, depth + 1)
            if node.left:
                dfs(node.left, depth + 1)
        
        dfs(root, 0)
        return right_view
```

## BFS Solution

```python
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        right_view = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            
            for i in range(level_size):
                node = queue.popleft()
                
                # Last node in level is rightmost
                if i == level_size - 1:
                    right_view.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return right_view
```

## Visual Intuition

### Example 1: Complete Tree

```
        1          Right Side View: [1, 3, 4]
       / \
      2   3        Level 0: [1] → 1 visible
       \           Level 1: [2, 3] → 3 visible
        4          Level 2: [4] → 4 visible
```

### Example 2: Left-Heavy Tree

```
        1          Right Side View: [1, 3, 5]
       / \
      2   3        Level 0: [1] → 1 visible
     /             Level 1: [2, 3] → 3 visible
    4              Level 2: [4] → 4 visible
   /               Level 3: [5] → 5 visible
  5                (Left child visible when no right child exists)
```

### Key Insight Visualization

```
Level Order:          Right Side View:
[[1],                 [1,
 [2, 3],        →      3,
 [4, 5, 6],            6,
 [7]]                  7]

Take last element of each level!
```

## Why This Works

The solution leverages the fact that:
1. **Level order traversal** visits all nodes at each depth
2. **Left-to-right traversal** ensures the rightmost node is last
3. **List comprehension** cleanly extracts the last element

The beauty is in reusing existing solutions - level order traversal becomes right side view with a simple transformation.

## Complexity Analysis

### Level Order Approach
- **Time Complexity:** O(n)
  - Level order traversal: O(n)
  - Extracting last elements: O(h) where h is height
  - Total: O(n)
- **Space Complexity:** O(n)
  - Storing all nodes in level order structure

### Optimized DFS
- **Time Complexity:** O(n)
  - Visit each node once
- **Space Complexity:** O(h)
  - Only stores one value per level
  - Recursion stack: O(h)

## Edge Cases

```python
# Edge Case 1: Empty tree
root = None
# Result: []

# Edge Case 2: Single node
root = TreeNode(1)
# Result: [1]

# Edge Case 3: Only left children (zigzag visibility)
#     1
#    /
#   2
#    \
#     3
# Result: [1, 2, 3]

# Edge Case 4: Only right children
#     1
#      \
#       2
#        \
#         3
# Result: [1, 2, 3]

# Edge Case 5: Complete binary tree
#       1
#      / \
#     2   3
#    / \ / \
#   4  5 6  7
# Result: [1, 3, 7]
```

## Common Mistakes

1. **Assuming only right children are visible**:
   ```python
   # Wrong: Only following right path
   def rightSideView(root):
       result = []
       while root:
           result.append(root.val)
           root = root.right  # Misses left children at deeper levels
   ```

2. **Not handling empty levels properly**:
   ```python
   # Wrong: IndexError on empty tree
   return [level[-1] for level in result]  # Fails if result is empty
   ```

3. **Wrong traversal order in optimization**:
   ```python
   # Wrong: Left-first means left child overwrites right
   if node.left:
       dfs(node.left, depth + 1)
   if node.right:  # This should be first!
       dfs(node.right, depth + 1)
   ```

## Pattern Recognition

This problem demonstrates:
- **View problems** - Extracting specific perspectives from trees
- **Level-based processing** - Using depth to group nodes
- **Solution reuse** - Building on existing algorithms

Similar problems:
- Binary Tree Left Side View (take first element)
- Binary Tree Top View (vertical order traversal)
- Binary Tree Bottom View
- Binary Tree Zigzag Level Order Traversal

## Optimization Trade-offs

| Approach | Time | Space | Pros | Cons |
|----------|------|-------|------|------|
| Level Order + Extract | O(n) | O(n) | Simple, reuses code | Stores all nodes |
| Optimized DFS | O(n) | O(h) | Space efficient | Less intuitive |
| BFS with Tracking | O(n) | O(w) | Natural level processing | Queue overhead |

## Key Insights

1. **Rightmost visibility** - Last node at each level is always visible from right

2. **Left children can be visible** - When no right children exist at that depth

3. **Level order foundation** - Many view problems build on level order traversal

4. **Traversal order matters** - Right-first DFS can optimize space

5. **Problem decomposition** - Complex problems often combine simpler solutions

## What I Learned

The solution effectively demonstrates problem decomposition - building complex solutions from simpler ones. Reusing level order traversal and taking the last element is straightforward and shows how understanding fundamental algorithms enables solving variations efficiently. The key insight that left children can be visible when there are no right children at that depth makes this more than just "follow the right path."