# Lowest Common Ancestor in Binary Search Tree

## Problem
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

The lowest common ancestor is defined between two nodes `p` and `q` as the lowest node in the tree that has both `p` and `q` as descendants (where we allow a node to be a descendant of itself).

## My Approach

I realized that in a BST, the LCA is the first node where p and q diverge (go to different subtrees). If both values are less than current node, LCA is on the left. If both are greater, LCA is on the right. Otherwise, the current node is the LCA (they diverge here).

## Corrected Solution with Comments

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Ensure p.val <= q.val for simpler comparisons
        if p.val > q.val:
            p, q = q, p
        
        self.common_ancestor = root
        
        def dfs(node):
            # Found the divergence point - this is the LCA
            if p.val <= node.val <= q.val:
                self.common_ancestor = node
            # Both values less than current - LCA is on left
            elif q.val < node.val:
                dfs(node.left)
            # Both values greater than current - LCA is on right
            elif p.val > node.val:
                dfs(node.right)
        
        dfs(root)
        return self.common_ancestor
```

## Cleaner Iterative Solution

```python
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        current = root
        
        while current:
            # Both nodes in left subtree
            if p.val < current.val and q.val < current.val:
                current = current.left
            # Both nodes in right subtree
            elif p.val > current.val and q.val > current.val:
                current = current.right
            # Found the split point (divergence)
            else:
                return current
```

## Even Cleaner Recursive Solution

```python
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Both on left side
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        # Both on right side
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        # Split point - this is the LCA
        else:
            return root
```

## Visual Intuition

### Example: BST with p=2, q=8

```
        6
       / \
      2   8
     / \ / \
    0  4 7  9
      / \
     3   5

Finding LCA(2, 8):
1. Start at root (6)
2. p=2 < 6 and q=8 > 6
3. They diverge here! LCA = 6
```

### Example: p=2, q=4

```
        6
       / \
      2   8
     / \ / \
    0  4 7  9
      / \
     3   5

Finding LCA(2, 4):
1. Start at root (6)
2. Both 2 < 6 and 4 < 6
3. Go left to node 2
4. p=2 = 2 and q=4 > 2
5. They diverge here! LCA = 2
```

### Key BST Property

```
For any node N in BST:
- All left descendants < N.val
- All right descendants > N.val

Therefore:
- If p,q < N: LCA is in left subtree
- If p,q > N: LCA is in right subtree  
- Otherwise: N is the LCA (split point)
```

## Why This Works

The insight is perfect: the LCA in a BST is the node where paths to p and q diverge. By ensuring p ≤ q, the logic is simplified:
1. If `p.val ≤ node.val ≤ q.val`: This is the split point
2. If both are smaller: Search left
3. If both are larger: Search right

## Complexity Analysis

### All Solutions
- **Time Complexity:** O(h)
  - h = height of tree
  - We follow one path from root to LCA
  - Best case (balanced): O(log n)
  - Worst case (skewed): O(n)
  
- **Space Complexity:** 
  - Recursive: O(h) for call stack
  - Iterative: O(1) - no extra space!

## Edge Cases

```python
# Edge Case 1: One node is ancestor of other
# p=2, q=4 where 2 is parent of 4
# LCA = 2 (ancestor can be its own descendant)

# Edge Case 2: p and q are same
# p=5, q=5
# LCA = 5

# Edge Case 3: Root is LCA
# Tree: 5
#      / \
#     3   7
# p=3, q=7
# LCA = 5

# Edge Case 4: Deep in same subtree
#       10
#      /
#     5
#    / \
#   3   7
# p=3, q=7
# LCA = 5
```

## Common Mistakes

1. **Wrong comparison logic**:
   ```python
   # Wrong: This condition never executes after swap
   elif (p.val <= node.val >= q.val):  # p ≤ q already!
   
   # Correct: Check if both are less
   elif q.val < node.val:
   ```

2. **Not handling equality**:
   ```python
   # Wrong: Misses case where p or q equals node
   if p.val < node.val and q.val > node.val:
   
   # Correct: Include equality
   if p.val <= node.val <= q.val:
   ```

3. **Unnecessary null checks**:
   ```python
   # Not needed in BST LCA (given p and q exist)
   if not node:
       return None
   ```

## Pattern Recognition

This problem demonstrates:
- **BST property exploitation** - Using ordering to navigate
- **Divergence point** - Finding where paths split
- **Binary search pattern** - Eliminating half the tree each step

Similar problems:
- LCA in Binary Tree (harder - no BST property)
- Distance Between Nodes in BST
- Validate BST (uses same property)
- Find Mode in BST

## Key Insights

1. **BST ordering is powerful** - Enables O(h) instead of O(n) solution

2. **Divergence = LCA** - The split point is always the answer

3. **No need to find nodes** - Just compare values and navigate

4. **Iterative is cleaner** - BST problems often have simple iterative solutions

5. **Swapping simplifies** - Ensuring p ≤ q reduces cases to handle

## What I Learned

The approach brilliantly uses the BST property - the LCA is simply where p and q diverge! The key was fixing the condition for "both on left side" to `q.val < node.val`. This problem shows how data structure properties (BST ordering) can dramatically simplify algorithms from O(n) to O(h).