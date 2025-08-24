# Binary Tree Level Order Traversal

## Problem
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

## My Approach

I used DFS with level tracking. As I traverse the tree, I keep track of the current level and append values to the appropriate level list in the result. If a level doesn't exist yet, I create it.

## Corrected Solution with Comments

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.result = []
        
        def dfs(node, level):
            # Check if we need to create a new level
            if len(self.result) == level:
                self.result.append([])
            
            # Add current node's value to its level
            self.result[level].append(node.val)
            
            # Traverse left subtree first (maintains left-to-right order)
            if node.left:
                dfs(node.left, level + 1)
            # Then traverse right subtree
            if node.right:
                dfs(node.right, level + 1)
        
        if root:
            dfs(root, 0)  # Start at level 0
        
        return self.result
```

## Alternative BFS Solution (Classic Approach)

```python
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            current_level = []
            
            # Process all nodes at current level
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)
                
                # Add children for next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(current_level)
        
        return result
```

## Visual Intuition

### Example Tree

```
        3
       / \
      9   20
         /  \
        15   7

DFS Traversal with Levels:
1. Visit 3 (level 0): result = [[3]]
2. Visit 9 (level 1): result = [[3], [9]]
3. Visit 20 (level 1): result = [[3], [9, 20]]
4. Visit 15 (level 2): result = [[3], [9, 20], [15]]
5. Visit 7 (level 2): result = [[3], [9, 20], [15, 7]]

Final: [[3], [9, 20], [15, 7]]
```

### DFS vs BFS Visualization

```
DFS with level tracking (your approach):
     1          Level 0: [1]
    / \         Level 1: [2, 3]
   2   3        Level 2: [4, 5]
  / \
 4   5

Visit order: 1 → 2 → 4 → 5 → 3
But grouped by level: [[1], [2,3], [4,5]]

BFS (traditional approach):
Visit order: 1 → 2 → 3 → 4 → 5
Natural level grouping: [[1], [2,3], [4,5]]
```

## Why This Works

The DFS approach cleverly:
1. **Tracks depth**: Passing level parameter maintains current depth
2. **Dynamic list creation**: Creates new level lists as needed
3. **In-order preservation**: Left-first traversal maintains left-to-right order
4. **Level grouping**: Despite depth-first traversal, groups by level

The key insight: DFS can solve level-order problems by tracking depth!

## Bug Fix Explanation

Original condition:
```python
if len(self.result) >= level:  # Wrong logic
    self.result[level-1].append(node.val)
```

Issues:
1. When `level=1` and `len(self.result)=0`: condition is False, creates new list (correct by accident)
2. When `level=2` and `len(self.result)=1`: condition is False, creates new list (correct)
3. But the indexing `level-1` assumes 1-based levels while checking 0-based length

Fixed version:
```python
if len(self.result) == level:  # Create new level when needed
    self.result.append([])
self.result[level].append(node.val)  # Use 0-based indexing
```

## Complexity Analysis

### DFS Solution
- **Time Complexity:** O(n)
  - Visit each node exactly once
- **Space Complexity:** O(n)
  - Result storage: O(n)
  - Recursion stack: O(h) where h is height
  - Total: O(n)

### BFS Solution
- **Time Complexity:** O(n)
- **Space Complexity:** O(w)
  - w = maximum width of tree
  - Queue holds at most one level

## Edge Cases

```python
# Edge Case 1: Empty tree
root = None
# Result: []

# Edge Case 2: Single node
root = TreeNode(1)
# Result: [[1]]

# Edge Case 3: Skewed tree (linked list)
#     1
#      \
#       2
#        \
#         3
# Result: [[1], [2], [3]]

# Edge Case 4: Complete binary tree
#       1
#      / \
#     2   3
#    / \ / \
#   4  5 6  7
# Result: [[1], [2,3], [4,5,6,7]]
```

## Common Mistakes

1. **Off-by-one level indexing**:
   ```python
   # Wrong: Mixing 0-based and 1-based
   if len(self.result) >= level:  # 0-based check
       self.result[level-1].append()  # 1-based index
   
   # Correct: Consistent indexing
   if len(self.result) == level:
       self.result.append([])
   self.result[level].append()
   ```

2. **Not checking if root exists**:
   ```python
   # Wrong: Crashes on None root
   def levelOrder(self, root):
       dfs(root, 0)
   
   # Correct: Check first
   if root:
       dfs(root, 0)
   ```

3. **Creating level list at wrong time**:
   ```python
   # Wrong: Creates after accessing
   self.result[level].append(node.val)  # IndexError!
   if len(self.result) == level:
       self.result.append([])
   
   # Correct: Create before accessing
   if len(self.result) == level:
       self.result.append([])
   self.result[level].append(node.val)
   ```

## Pattern Recognition

This problem demonstrates:
- **Level-order traversal** - Grouping nodes by depth
- **DFS with metadata** - Tracking additional info during traversal
- **BFS natural fit** - Queue-based approach matches problem structure

Similar problems:
- Binary Tree Zigzag Level Order Traversal
- Binary Tree Right Side View (last element of each level)
- Average of Levels in Binary Tree
- Maximum Depth (count levels)

## Key Insights

1. **DFS can do level-order** - With level tracking, DFS solves BFS problems

2. **Pre-order maintains order** - Left-first traversal preserves left-to-right

3. **Dynamic list growth** - Creating levels as needed handles any tree shape

4. **Level as index** - Using level directly as index simplifies logic

5. **Both approaches valid** - DFS and BFS both solve it efficiently

## What I Learned

● **Learn by Doing**

**Context:** I've set up both DFS and BFS solutions for level-order traversal. The DFS approach uses level tracking while BFS naturally processes level by level. Now we need to explore when each approach is better.

**Your Task:** In binary_tree_level_order_traversal.md, implement a comparison section that analyzes memory usage. Look for TODO(human).

**Guidance:** Consider the recursion stack depth for DFS vs queue size for BFS. Think about best and worst case scenarios (balanced vs skewed trees). Which approach uses less memory for a very wide tree? Which for a very deep tree?

```python
# TODO(human): Add memory comparison here
# For a tree with height h and max width w:
# DFS stack space: ?
# BFS queue space: ?
```

---

The DFS solution with level tracking is elegant! The key fix was changing the condition to check when to create a new level. The insight that DFS can solve level-order problems by tracking depth shows great problem-solving flexibility. The choice between DFS and BFS often comes down to the specific tree shape and memory constraints.