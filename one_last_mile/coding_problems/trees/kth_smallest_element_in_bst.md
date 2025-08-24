# Kth Smallest Element in a BST

## Problem
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

## My Approach

I use inorder traversal since it visits BST nodes in ascending order. I maintain a counter and stop as soon as I reach the kth node, avoiding unnecessary traversal of the remaining tree.

## Solution with Comments

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.kth_item = None
        
        def inorder_traversal(node):
            # Early termination: stop if node is None or answer found
            if not node or self.kth_item is not None:
                return
            
            # Traverse left subtree (smaller values)
            inorder_traversal(node.left)
            
            # Process current node
            self.count += 1
            if self.count == k:
                self.kth_item = node.val
                return  # Found kth smallest, stop traversal
            
            # Traverse right subtree (larger values)
            inorder_traversal(node.right)
        
        inorder_traversal(root)
        return self.kth_item
```

## Alternative Solution - Iterative with Stack

```python
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        current = root
        count = 0
        
        while stack or current:
            # Go to leftmost node
            while current:
                stack.append(current)
                current = current.left
            
            # Process node
            current = stack.pop()
            count += 1
            if count == k:
                return current.val
            
            # Move to right subtree
            current = current.right
        
        return -1  # Should never reach here with valid input
```

## Visual Intuition

### Example: Find 3rd Smallest

```
        5
       / \
      3   6
     / \
    2   4
   /
  1

Inorder traversal: 1, 2, 3, 4, 5, 6

Step-by-step:
1. Go left to 3, then to 2, then to 1
2. Visit 1: count=1 (not k)
3. Visit 2: count=2 (not k)  
4. Visit 3: count=3 (equals k!)
5. Set kth_item = 3 and terminate

Result: 3 (the 3rd smallest element)
```

### Early Termination Visualization

```
        10
       /  \
      5    15
     / \   / \
    3   7 12  20
   /|   |\ |\ |\
  [many more nodes...]
  
Finding k=2:
- Visit 3: count=1
- Visit 5: count=2 ✓ Found!
- Skip visiting 7, 10, 12, 15, 20, etc.
```

## Why This Works

The solution leverages two key insights:
1. **BST Property**: Inorder traversal visits nodes in ascending order
2. **Early Termination**: Once kth element is found, checking `self.kth_item is not None` prevents further traversal

The termination check appears in two places:
- In the condition: stops entering new recursive calls
- After finding kth: immediate return (though recursion unwinds anyway)

## Complexity Analysis

- **Time Complexity:** O(h + k)
  - h = height to reach the leftmost node
  - k = number of nodes to visit in order
  - Best case: O(k) when k is small
  - Worst case: O(n) when k = n
  
- **Space Complexity:** O(h)
  - Recursion stack depth
  - Best case (balanced): O(log n)
  - Worst case (skewed): O(n)

## Optimization for Multiple Queries

If you need to find kth smallest multiple times on the same tree:

```python
class BSTWithCount:
    def __init__(self, root):
        # Augment tree nodes with subtree sizes
        self.root = root
        self._add_counts(root)
    
    def _add_counts(self, node):
        if not node:
            return 0
        left_count = self._add_counts(node.left)
        right_count = self._add_counts(node.right)
        node.count = 1 + left_count + right_count
        return node.count
    
    def kthSmallest(self, k):
        node = self.root
        while node:
            left_count = node.left.count if node.left else 0
            if k <= left_count:
                node = node.left
            elif k == left_count + 1:
                return node.val
            else:
                k -= left_count + 1
                node = node.right
```

This allows O(h) queries after O(n) preprocessing.

## Edge Cases

```python
# Edge Case 1: k = 1 (minimum element)
#     2
#    /
#   1
# Result: 1 (leftmost node)

# Edge Case 2: k = n (maximum element)  
#     1
#      \
#       2
# Result: 2 (rightmost node)

# Edge Case 3: Single node tree
root = TreeNode(5), k = 1
# Result: 5

# Edge Case 4: Balanced tree
#       4
#      / \
#     2   6
#    / \ / \
#   1  3 5  7
# k=4 → Result: 4 (root happens to be 4th)
```

## Common Mistakes

1. **Forgetting early termination**:
   ```python
   # Inefficient: Traverses entire tree
   def inorder_traversal(node):
       if not node:
           return
       inorder_traversal(node.left)
       self.count += 1
       if self.count == k:
           self.kth_item = node.val
       inorder_traversal(node.right)  # Continues even after finding answer
   ```

2. **Using preorder or postorder**:
   ```python
   # Wrong: Preorder doesn't give sorted sequence in BST
   def preorder(node):
       self.count += 1  # Process before children - wrong order!
       if self.count == k:
           self.kth_item = node.val
   ```

3. **Off-by-one error**:
   ```python
   # Wrong: Starting count at 1
   self.count = 1  # Should start at 0
   ```

## Pattern Recognition

This problem demonstrates:
- **BST inorder = sorted** - Fundamental BST property
- **Early termination** - Optimization to avoid unnecessary work
- **Counter pattern** - Tracking position in traversal
- **Global state** - Using class variables for cross-recursion communication

Similar problems:
- Validate Binary Search Tree (uses inorder)
- Convert BST to Greater Tree (reverse inorder)
- Inorder Successor in BST
- Range Sum of BST

## Key Insights

1. **Inorder traversal gives sorted order** - The core insight for BST problems

2. **Early termination is crucial** - For small k, avoids traversing most of the tree

3. **Counter tracks position** - Simple way to identify kth element

4. **Class variables enable communication** - Clean way to pass results up recursion

5. **BST structure enables optimization** - Unlike general binary trees

## What I Learned

The solution efficiently finds the kth smallest element by combining BST properties with early termination. The check `self.kth_item is not None` in the entry condition is particularly effective - it prevents entering new recursive calls once the answer is found. This pattern of using a flag to terminate recursive traversal early is useful in many tree problems where you don't need to visit all nodes.