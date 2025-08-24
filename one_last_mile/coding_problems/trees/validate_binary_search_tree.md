# Validate Binary Search Tree

## Problem
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:
- The left subtree of a node contains only nodes with keys less than the node's key
- The right subtree of a node contains only nodes with keys greater than the node's key
- Both the left and right subtrees must also be binary search trees

## My Approach

I used inorder traversal since a valid BST's inorder traversal yields strictly increasing values. Instead of storing all values, I check them on-the-fly by comparing each node with the previous value.

## Solution with Comments (Optimized)

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Track the previous value in inorder traversal
        self.prev = float('-inf')
        
        def in_order_traversal(node):
            if not node:
                return True
            
            # Traverse left subtree first
            if not in_order_traversal(node.left):
                return False
            
            # Check if current value > previous (strictly increasing)
            if node.val > self.prev:
                self.prev = node.val
            else:
                return False  # Not strictly increasing = invalid BST
            
            # Traverse right subtree
            if not in_order_traversal(node.right):
                return False
            
            return True
        
        return in_order_traversal(root)
```

## Initial Approach (Store All Values)

```python
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        values = []
        
        def in_order_traversal(node):
            if not node:
                return
            in_order_traversal(node.left)
            values.append(node.val)
            in_order_traversal(node.right)
        
        in_order_traversal(root)
        
        # Check if array is strictly increasing
        for i in range(1, len(values)):
            if values[i] <= values[i-1]:
                return False
        
        return True
```

## Alternative Approach - Bounds Checking

```python
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, min_val, max_val):
            if not node:
                return True
            
            # Check if node violates BST property
            if node.val <= min_val or node.val >= max_val:
                return False
            
            # Left subtree: all values must be < node.val
            # Right subtree: all values must be > node.val
            return (validate(node.left, min_val, node.val) and 
                   validate(node.right, node.val, max_val))
        
        return validate(root, float('-inf'), float('inf'))
```

## Visual Intuition

### Valid BST Example

```
        5
       / \
      3   8
     / \ / \
    2  4 7  9

Inorder: [2, 3, 4, 5, 7, 8, 9] ✓ Strictly increasing
```

### Invalid BST Example

```
        5
       / \
      3   8
     / \ / \
    2  6 7  9
       ^
       6 > 5 (violates BST property)

Inorder: [2, 3, 6, 5, 7, 8, 9] ✗ Not strictly increasing
```

### Step-by-Step Trace (Optimized Solution)

```
Tree:     5
         / \
        1   7
           / \
          6   8

Traverse:
1. Go left to 1
2. Visit 1: prev=-∞, 1>-∞ ✓, prev=1
3. Visit 5: prev=1, 5>1 ✓, prev=5
4. Go right to 7
5. Visit 6: prev=5, 6>5 ✓, prev=6
6. Visit 7: prev=6, 7>6 ✓, prev=7
7. Visit 8: prev=7, 8>7 ✓, prev=8

Result: Valid BST
```

## Why Inorder Traversal Works

The key insight is that inorder traversal of a BST visits nodes in ascending order:
1. **Left subtree** (smaller values)
2. **Current node**
3. **Right subtree** (larger values)

If the tree is a valid BST, this produces a strictly increasing sequence. Any violation means the BST property is broken.

## Complexity Analysis

### Optimized Solution (Checking On-the-fly)
- **Time Complexity:** O(n)
  - Visit each node exactly once
- **Space Complexity:** O(h)
  - Recursion stack depth
  - No additional storage for values

### Initial Solution (Store All Values)
- **Time Complexity:** O(n)
  - Traverse: O(n) + Check array: O(n)
- **Space Complexity:** O(n)
  - Store all node values

### Bounds Checking Solution
- **Time Complexity:** O(n)
- **Space Complexity:** O(h)

## Edge Cases

```python
# Edge Case 1: Single node
root = TreeNode(5)
# Result: True (single node is valid BST)

# Edge Case 2: Duplicate values
#     5
#    / \
#   5   5
# Result: False (BST requires strict inequality)

# Edge Case 3: Right child less than ancestor
#       10
#      /
#     5
#      \
#       7  (valid locally but 7 < 10 required)
# Result: True (7 is between 5 and 10)

# Edge Case 4: Integer overflow
root = TreeNode(2147483647)  # INT_MAX
# Result: True (handle with float('-inf'))

# Edge Case 5: Subtree violation
#       5
#      / \
#     3   8
#    /
#   7  (7 > 5, violates BST property)
# Result: False
```

## Common Mistakes

1. **Using non-strict inequality**:
   ```python
   # Wrong: Allows duplicates
   if node.val >= self.prev:
   
   # Correct: Strict inequality for BST
   if node.val > self.prev:
   ```

2. **Not checking all ancestors**:
   ```python
   # Wrong: Only checks immediate parent
   def isValid(node):
       if node.left and node.left.val >= node.val:
           return False
       if node.right and node.right.val <= node.val:
           return False
   
   # Correct: Must validate against all ancestors
   ```

3. **Wrong initial value**:
   ```python
   # Wrong: Assumes all values > 0
   self.prev = 0
   
   # Correct: Handle all possible values
   self.prev = float('-inf')
   ```

## Pattern Recognition

This problem demonstrates:
- **BST property validation** - Understanding what makes a valid BST
- **Inorder traversal application** - Using traversal properties
- **Global vs local validation** - Node must satisfy constraints from all ancestors

Similar problems:
- Kth Smallest Element in BST (uses inorder)
- Recover Binary Search Tree
- Convert BST to Greater Tree
- Validate Binary Tree Nodes

## Key Insights

1. **Inorder = Sorted** - Fundamental property of BSTs

2. **Global constraints** - Each node must respect all ancestor bounds

3. **Space optimization** - No need to store all values

4. **Early termination** - Return false immediately on violation

5. **Strict inequality** - BSTs don't allow duplicates

## What I Learned

The inorder traversal approach elegantly validates BSTs by leveraging their fundamental property - sorted traversal order. The optimization from storing all values to checking on-the-fly shows good space complexity awareness. The alternative bounds-checking approach demonstrates that the same problem can be solved by thinking about constraints differently - either checking sorted order or validating bounds. Both approaches highlight the importance of understanding data structure properties.