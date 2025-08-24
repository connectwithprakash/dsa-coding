# Diameter of Binary Tree

## Problem
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

## My Approach

I realized that the diameter at any node is the sum of the heights of its left and right subtrees. While computing heights recursively, I track the maximum diameter seen so far using a class variable. This allows me to find the global maximum while doing a single traversal.

## Solution with Comments

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Track the maximum diameter seen so far
        self.diameter = 0
        
        def dfs(node):
            # Base case: None has height 0
            if node is None:
                return 0
            
            # Get heights of left and right subtrees
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            
            # Diameter through this node is sum of left and right heights
            # Update global maximum if this is larger
            self.diameter = max(self.diameter, left_height + right_height)
            
            # Return height of current subtree for parent's calculation
            return 1 + max(left_height, right_height)
        
        dfs(root)
        return self.diameter
```

## Visual Intuition

### Example 1: Diameter Passes Through Root

```
        1
       / \
      2   3
     / \
    4   5

Heights and Diameters:
- Node 4: height=0, diameter through it = 0+0 = 0
- Node 5: height=0, diameter through it = 0+0 = 0
- Node 2: height=1, diameter through it = 1+1 = 2
- Node 3: height=0, diameter through it = 0+0 = 0
- Node 1: height=2, diameter through it = 2+1 = 3

Maximum diameter = 3 (path: 4→2→1→3 or 5→2→1→3)
```

### Example 2: Diameter Doesn't Pass Through Root

```
           1
          /
         2
        / \
       4   5
      /
     6

Heights and Diameters:
- Node 6: height=0, diameter = 0
- Node 4: height=1, diameter = 1+0 = 1
- Node 5: height=0, diameter = 0
- Node 2: height=2, diameter = 2+1 = 3
- Node 1: height=3, diameter = 3+0 = 3

Maximum diameter = 3 (path: 6→4→2→5)
```

### Key Insight Visualization

```
At each node:
     node
     /  \
   left  right
   
Diameter through node = left_height + right_height
Height of node = 1 + max(left_height, right_height)

We need BOTH values:
- Diameter for finding the answer
- Height for parent's diameter calculation
```

## Why Your Solution Works

The brilliance is in tracking two different metrics:
1. **Height** (returned): Used by parent nodes for their calculations
2. **Diameter** (tracked globally): The actual answer we're looking for

At each node, you:
- Calculate the potential diameter passing through it (left_height + right_height)
- Update the global maximum if this diameter is larger
- Return the height for the parent's use

## Alternative Approach - Using Return Values

```python
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0, 0  # (height, diameter)
            
            left_height, left_diameter = dfs(node.left)
            right_height, right_diameter = dfs(node.right)
            
            # Current height
            height = 1 + max(left_height, right_height)
            
            # Best diameter is max of:
            # 1. Left subtree's diameter
            # 2. Right subtree's diameter  
            # 3. Path through current node
            diameter = max(left_diameter, right_diameter, 
                          left_height + right_height)
            
            return height, diameter
        
        _, diameter = dfs(root)
        return diameter
```

## Complexity Analysis

- **Time Complexity:** O(n)
  - Visit each node exactly once
  - O(1) operations per node
  
- **Space Complexity:** O(h)
  - Recursion stack depth equals tree height
  - Best case (balanced): O(log n)
  - Worst case (skewed): O(n)

## Edge Cases

```python
# Edge Case 1: Single node
root = TreeNode(1)
# Diameter = 0 (no edges)

# Edge Case 2: Two nodes
#   1
#  /
# 2
# Diameter = 1 (one edge)

# Edge Case 3: Skewed tree (linked list)
#     1
#      \
#       2
#        \
#         3
# Diameter = 2 (1→2→3)

# Edge Case 4: Complete binary tree
#       1
#      / \
#     2   3
#    / \ / \
#   4  5 6  7
# Diameter = 4 (4→2→1→3→6 or similar)
```

## Common Mistakes

1. **Confusing diameter with height**:
   ```python
   # Wrong: Returning diameter instead of height
   return 1 + max(left_height, right_height) + 1
   
   # Correct: Return height, track diameter separately
   return 1 + max(left_height, right_height)
   ```

2. **Forgetting edges vs nodes**:
   ```python
   # Wrong: Counting nodes instead of edges
   self.diameter = max(self.diameter, left_height + right_height + 1)
   
   # Correct: Edges = sum of heights
   self.diameter = max(self.diameter, left_height + right_height)
   ```

3. **Not considering diameter might not pass through root**:
   ```python
   # Wrong: Only checking at root
   return dfs(root.left) + dfs(root.right)
   
   # Correct: Check at every node
   self.diameter = max(self.diameter, left_height + right_height)
   ```

## Pattern Recognition

This problem demonstrates:
- **Global tracking during recursion** - Using class variable for global maximum
- **Dual-purpose DFS** - Computing one value while tracking another
- **Post-order traversal** - Need subtree info before processing node

Similar problems:
- Maximum Path Sum (track sum instead of length)
- Balanced Binary Tree (track height and balance)
- Longest Univalue Path (diameter with value constraint)
- Binary Tree Maximum Width (level-based instead of path-based)

## Key Insights

1. **Height vs Diameter** - Height helps calculate diameter, but they're different metrics

2. **Global maximum pattern** - Class variable elegantly tracks the best answer seen

3. **Single traversal sufficiency** - No need to compute diameter separately at each node

4. **Path decomposition** - Any path can be decomposed into left path + right path at some node

5. **Edge counting** - Diameter counts edges, not nodes (easy to confuse!)

## What I Learned

Your solution elegantly solves a tricky problem where the answer isn't necessarily at the root. The pattern of computing one value (height) while tracking another (diameter) is powerful and appears in many tree problems. Using a class variable to track the global maximum during recursion is cleaner than passing it as a parameter or returning tuples. The key insight that diameter = left_height + right_height makes the solution surprisingly simple once you see it.