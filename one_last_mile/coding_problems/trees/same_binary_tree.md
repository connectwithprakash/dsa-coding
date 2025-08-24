# Same Binary Tree

## Problem
Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

## My Approach

I used recursion to compare both trees simultaneously. At each position, I check if both nodes are None (same), if only one is None (different), or if values differ (different). If all checks pass, I recursively verify both left and right subtrees.

## Solution with Comments

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def compare_subtree(p, q):
            # Both nodes are None - identical at this position
            if not p and not q:
                return True
            
            # One is None but not the other, or values differ - not identical
            if (p and not q) or (not p and q) or (p.val != q.val):
                return False
            
            # Both nodes exist and have same value - check children
            return compare_subtree(p.left, q.left) and compare_subtree(p.right, q.right)
        
        return compare_subtree(p, q)
```

## More Concise Version

```python
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base cases
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        
        # Recursive case
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
```

## Visual Intuition

### Example 1: Same Trees

```
Tree p:        Tree q:
    1              1
   / \            / \
  2   3          2   3

Comparison flow:
- Compare roots: 1 == 1 ✓
- Compare left children: 2 == 2 ✓
- Compare right children: 3 == 3 ✓
- All checks pass → True
```

### Example 2: Different Structure

```
Tree p:        Tree q:
    1              1
   /                \
  2                  2

Comparison flow:
- Compare roots: 1 == 1 ✓
- Compare left: 2 vs None ✗
- Different structure → False
```

### Example 3: Different Values

```
Tree p:        Tree q:
    1              1
   / \            / \
  2   1          2   3

Comparison flow:
- Compare roots: 1 == 1 ✓
- Compare left: 2 == 2 ✓
- Compare right: 1 != 3 ✗
- Different values → False
```

## Why This Works

The solution cleverly handles all cases in the condition check:
1. **Both None**: Trees are same at this position
2. **Structure mismatch**: `(p and not q) or (not p and q)` catches when only one is None
3. **Value mismatch**: `p.val != q.val` catches different values
4. **Recursive verification**: AND operation ensures all subtrees must match

The beauty is in the short-circuit evaluation - if any condition fails, we immediately return False.

## Alternative Approach - Iterative with Stack

```python
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p, q)]
        
        while stack:
            node1, node2 = stack.pop()
            
            # Both None - continue to next pair
            if not node1 and not node2:
                continue
            
            # Structure or value mismatch
            if not node1 or not node2 or node1.val != node2.val:
                return False
            
            # Add children pairs to stack
            stack.append((node1.left, node2.left))
            stack.append((node1.right, node2.right))
        
        return True
```

## Complexity Analysis

### Recursive Solution
- **Time Complexity:** O(min(m, n))
  - m and n are the number of nodes in trees p and q
  - We stop as soon as a difference is found
  - Worst case: traverse entire smaller tree
  
- **Space Complexity:** O(min(m, n))
  - Recursion stack depth
  - In worst case (skewed), equals the height of smaller tree

### Iterative Solution
- **Time Complexity:** O(min(m, n))
- **Space Complexity:** O(min(m, n))
  - Stack can hold at most all nodes of smaller tree

## Edge Cases

```python
# Edge Case 1: Both empty
p = None, q = None
# Result: True

# Edge Case 2: One empty
p = TreeNode(1), q = None
# Result: False

# Edge Case 3: Single nodes same
p = TreeNode(1), q = TreeNode(1)
# Result: True

# Edge Case 4: Single nodes different
p = TreeNode(1), q = TreeNode(2)
# Result: False

# Edge Case 5: Same structure, different values deep in tree
#     1           1
#    / \         / \
#   2   3       2   3
#  /           /
# 4           5
# Result: False (difference at leaf level)
```

## Common Mistakes

1. **Not checking both None first**:
   ```python
   # Wrong: Will crash on p.val when p is None
   if p.val != q.val:
       return False
   
   # Correct: Check None cases first
   if not p and not q:
       return True
   ```

2. **Using OR instead of AND for recursion**:
   ```python
   # Wrong: Returns True if ANY subtree matches
   return compare(p.left, q.left) or compare(p.right, q.right)
   
   # Correct: ALL subtrees must match
   return compare(p.left, q.left) and compare(p.right, q.right)
   ```

3. **Incomplete None checking**:
   ```python
   # Wrong: Doesn't catch case where only one is None
   if not p and not q:
       return True
   if p.val != q.val:  # Crashes if p or q is None!
       return False
   
   # Correct: Check all None cases
   if (p and not q) or (not p and q):
       return False
   ```

## Pattern Recognition

This problem demonstrates:
- **Parallel tree traversal** - Processing two trees simultaneously
- **Structural comparison** - Checking both shape and values
- **Early termination** - Stop as soon as difference found

Similar problems:
- Subtree of Another Tree (uses this as a subroutine)
- Symmetric Tree (compare tree with its mirror)
- Merge Two Binary Trees (combine instead of compare)
- Leaf-Similar Trees (compare only leaves)

## Key Insights

1. **Order matters** - Check None cases before accessing values

2. **Short-circuit evaluation** - AND ensures first False stops recursion

3. **Parallel recursion** - Navigate both trees in lockstep

4. **Structural and value equality** - Must match both shape and content

5. **Base case elegance** - Your combined condition handles multiple cases cleanly

## What I Learned

● **Learn by Doing**

**Context:** I've set up the tree comparison logic that handles all the edge cases. The recursive structure is ready, but we need to decide on the comparison strategy for handling mismatches efficiently.

**Your Task:** In same_tree.md, implement an optimization section that explores whether we should check values first or structure first for better performance. Look for TODO(human).

**Guidance:** Consider the probability of value mismatches vs structural mismatches in typical use cases. Think about which check is cheaper and whether order matters for short-circuit evaluation. Your analysis should help readers understand the performance implications of check ordering.

---

The solution elegantly solves the tree comparison problem with minimal code. The combined condition `(p and not q) or (not p and q) or (p.val != q.val)` is particularly clever - it handles three different failure cases in one line. This shows that sometimes the most straightforward recursive approach is also the most elegant.