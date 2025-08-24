# Maximum Depth of Binary Tree

## Problem
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

## My Approach

I used recursion to find the depth. The maximum depth at any node is 1 (for the current node) plus the maximum depth of its subtrees. The base case is when we reach None, which has depth 0.

## Solution

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base case: empty tree has depth 0
        if root is None:
            return 0
        
        # Recursively find depth of left subtree
        left_depth = self.maxDepth(root.left)
        # Recursively find depth of right subtree
        right_depth = self.maxDepth(root.right)
        
        # Current node adds 1 to the maximum depth of its subtrees
        return 1 + max(left_depth, right_depth)
```

## More Concise Version

```python
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
```

## Visual Intuition

### Example Tree

```
        3
       / \
      9   20
         /  \
        15   7

Depth Calculation:
- Node 15: depth = 1 (leaf)
- Node 7: depth = 1 (leaf)
- Node 9: depth = 1 (leaf)
- Node 20: depth = 1 + max(depth(15), depth(7)) = 1 + max(1, 1) = 2
- Node 3: depth = 1 + max(depth(9), depth(20)) = 1 + max(1, 2) = 3

Maximum Depth = 3
```

### Recursion Flow

```
maxDepth(3)
├── maxDepth(9)
│   ├── maxDepth(None) → 0
│   ├── maxDepth(None) → 0
│   └── returns: 1 + max(0, 0) = 1
├── maxDepth(20)
│   ├── maxDepth(15)
│   │   ├── maxDepth(None) → 0
│   │   ├── maxDepth(None) → 0
│   │   └── returns: 1 + max(0, 0) = 1
│   ├── maxDepth(7)
│   │   ├── maxDepth(None) → 0
│   │   ├── maxDepth(None) → 0
│   │   └── returns: 1 + max(0, 0) = 1
│   └── returns: 1 + max(1, 1) = 2
└── returns: 1 + max(1, 2) = 3
```

## Alternative Approaches

### Iterative BFS (Level-Order Traversal)

```python
from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = deque([root])
        depth = 0
        
        while queue:
            depth += 1
            # Process all nodes at current level
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return depth
```

### Iterative DFS (Using Stack)

```python
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        stack = [(root, 1)]  # (node, current_depth)
        max_depth = 0
        
        while stack:
            node, current_depth = stack.pop()
            max_depth = max(max_depth, current_depth)
            
            if node.left:
                stack.append((node.left, current_depth + 1))
            if node.right:
                stack.append((node.right, current_depth + 1))
        
        return max_depth
```

## Why This Works

The recursive approach naturally follows the tree structure:
1. **Base case**: Empty tree has depth 0
2. **Recursive case**: Each node adds 1 to the maximum depth of its children
3. **Bottom-up computation**: Depths are calculated from leaves up to root

This is a post-order traversal where we:
- First compute depths of subtrees
- Then use those results to compute current node's contribution

## Complexity Analysis

### Recursive Solution
- **Time Complexity:** O(n)
  - Visit every node exactly once
  - O(1) work per node (comparison and addition)
- **Space Complexity:** O(h)
  - Recursion stack depth equals tree height
  - Best case (balanced): O(log n)
  - Worst case (skewed): O(n)

### BFS Solution
- **Time Complexity:** O(n)
  - Process every node once
- **Space Complexity:** O(w)
  - Queue holds at most one level
  - w = maximum width of tree
  - Worst case: O(n/2) for perfect binary tree

### DFS Iterative
- **Time Complexity:** O(n)
- **Space Complexity:** O(h)
  - Stack mimics recursion depth

## Edge Cases

```python
# Edge Case 1: Empty tree
root = None
# Result: 0

# Edge Case 2: Single node
root = TreeNode(1)
# Result: 1

# Edge Case 3: Skewed tree (linked list-like)
#     1
#      \
#       2
#        \
#         3
# Result: 3

# Edge Case 4: Perfect binary tree
#       1
#      / \
#     2   3
#    / \ / \
#   4  5 6  7
# Result: 3

# Edge Case 5: Only left children
#     1
#    /
#   2
#  /
# 3
# Result: 3
```

## Key Insights

1. **Depth vs Height** - This problem asks for depth (nodes count) not height (edges count)

2. **Post-order pattern** - Calculate children first, then use results for parent

3. **Max operation** - Automatically handles unbalanced trees by taking the deeper path

4. **Simplicity wins** - The recursive solution is cleaner than iterative alternatives

5. **Natural recursion** - Tree problems often have clean recursive solutions

## Common Mistakes

1. **Confusing depth with height**:
   ```python
   # Wrong: Counting edges instead of nodes
   if not root:
       return -1  # Should be 0
   ```

2. **Forgetting the +1**:
   ```python
   # Wrong: Not counting current node
   return max(self.maxDepth(root.left), self.maxDepth(root.right))
   # Correct: Add 1 for current node
   return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
   ```

3. **Not handling None base case**:
   ```python
   # Wrong: Will crash on None
   def maxDepth(self, root):
       return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
   ```

## Pattern Recognition

This problem demonstrates:
- **Tree traversal** - Classic DFS recursion
- **Bottom-up computation** - Use subtree results to compute parent
- **Divide and conquer** - Break into subproblems (left and right subtrees)

Similar problems:
- Minimum Depth of Binary Tree (min instead of max)
- Balanced Binary Tree (check if depth difference ≤ 1)
- Diameter of Binary Tree (longest path between any two nodes)
- Maximum Path Sum (similar recursion pattern)

## What I Learned

The simplicity of the solution shows how naturally recursion fits tree problems. The pattern of "process subtrees, then combine results" appears in many tree problems. Breaking down the depth calculation into clear steps (get left depth, get right depth, return 1 + max) makes the logic crystal clear. This problem is a perfect introduction to tree recursion - simple enough to understand but fundamental enough to build upon for more complex problems.