# Subtree of Another Tree

## Problem
Given the roots of two binary trees `root` and `subRoot`, return true if there is a subtree of `root` with the same structure and node values of `subRoot` and false otherwise.

A subtree of a binary tree `tree` is a tree that consists of a node in `tree` and all of this node's descendants. The tree `tree` could also be considered as a subtree of itself.

## My Approach

I realized this problem builds on the Same Binary Tree problem. For each node in the main tree, I check if the subtree rooted at that node matches `subRoot`. I reuse my `isSameTree` function and traverse the main tree with DFS, checking for matches.

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
        # Base cases
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        
        # Recursive case - both subtrees must match
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(node):
            # Base case: reached end of tree without finding match
            if not node:
                return False
            
            # When values match, check if entire subtrees are same
            if node.val == subRoot.val:
                is_subtree = self.isSameTree(node, subRoot)
                # Important: continue searching even if not same
                # The actual subtree might be deeper
                return is_subtree or dfs(node.left) or dfs(node.right)
            else:
                # Values don't match, keep searching in children
                return dfs(node.left) or dfs(node.right)
        
        return dfs(root)
```

## Cleaner Version

```python
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Edge case: empty subRoot matches any tree
        if not subRoot:
            return True
        # Edge case: empty root can't contain non-empty subRoot
        if not root:
            return False
        
        # Check current position or search in children
        if self.isSameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
```

## Visual Intuition

### Example 1: Subtree Found

```
Main Tree:          SubRoot:
     3                 4
    / \               / \
   4   5             1   2
  / \
 1   2

Search Process:
1. Check node 3: values differ (3 != 4), search children
2. Check node 4: values match (4 == 4)
   - Run isSameTree(node_4_subtree, subRoot)
   - Structure matches! Return True
```

### Example 2: Value Match but Not Subtree

```
Main Tree:          SubRoot:
     3                 4
    / \               / \
   4   5             1   2
  / \                    /
 1   2                  6
    /
   6

Search Process:
1. Check node 3: values differ, search children
2. Check node 4: values match (4 == 4)
   - Run isSameTree - fails (different structure)
   - Continue searching in children
3. Check nodes 1, 2, 6, 5: no matches
Result: False
```

### Key Insight - Continue After Failed Match

```
     1
    / \
   4   4  ← This 4 matches subRoot
  /     \
 2       1
        / \
       2   3

subRoot:
   4
  / \
 1   3

Even though first 4 doesn't match the pattern,
we must continue to find the second 4 which does!
```

## Why This Works

The brilliance is in the logic flow:
1. **Value matching as a filter**: Only run expensive `isSameTree` when values match
2. **Continue searching after failure**: `is_subtree or dfs(node.left) or dfs(node.right)` ensures we don't stop at first value match
3. **OR chain for propagation**: Any True result bubbles up immediately

## Complexity Analysis

- **Time Complexity:** O(m * n)
  - m = nodes in main tree, n = nodes in subRoot
  - Worst case: check isSameTree at every node
  - Each isSameTree check is O(n)
  
- **Space Complexity:** O(m)
  - Recursion depth for main tree traversal
  - Additional O(min(m, n)) for isSameTree calls

## Alternative Approach - Serialization

```python
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def serialize(node):
            if not node:
                return "#"
            # Use delimiters to avoid false matches
            return f",{node.val},{serialize(node.left)},{serialize(node.right)}"
        
        # Check if subRoot serialization is substring of root serialization
        return serialize(subRoot) in serialize(root)
```

**Note**: This is O(m + n) time but uses more space and requires careful delimiter handling.

## Edge Cases

```python
# Edge Case 1: subRoot is None
root = TreeNode(1), subRoot = None
# Result: True (empty tree is subtree of any tree)

# Edge Case 2: root is None
root = None, subRoot = TreeNode(1)
# Result: False (non-empty can't be subtree of empty)

# Edge Case 3: Single node match
root = TreeNode(1), subRoot = TreeNode(1)
# Result: True

# Edge Case 4: Value appears multiple times
#      4
#     / \
#    4   4
#   /
#  4
# subRoot = TreeNode(4)
# Result: True (matches at leaf)

# Edge Case 5: Partial match
#      1
#     / \
#    2   3
#   /
#  4
# subRoot: 2->4->5
# Result: False (structure differs)
```

## Common Mistakes

1. **Stopping at first value match**:
   ```python
   # Wrong: Returns False if first match fails
   if node.val == subRoot.val:
       return self.isSameTree(node, subRoot)
   
   # Correct: Continue searching if match fails
   return is_subtree or dfs(node.left) or dfs(node.right)
   ```

2. **Not checking the current node**:
   ```python
   # Wrong: Only checks children
   return dfs(node.left) or dfs(node.right)
   
   # Correct: Check current node too
   is_subtree = self.isSameTree(node, subRoot)
   return is_subtree or dfs(node.left) or dfs(node.right)
   ```

3. **Using AND instead of OR**:
   ```python
   # Wrong: Requires subtree in BOTH children
   return dfs(node.left) and dfs(node.right)
   
   # Correct: Subtree can be in EITHER child
   return dfs(node.left) or dfs(node.right)
   ```

## Pattern Recognition

This problem demonstrates:
- **Problem composition** - Using one problem's solution (Same Tree) to solve another
- **Tree searching** - Finding a pattern within a larger structure
- **Short-circuit evaluation** - OR chain stops at first True

Similar problems:
- Same Binary Tree (used as helper)
- Find Duplicate Subtrees
- Most Frequent Subtree Sum
- Binary Tree Paths (different kind of search)

## Optimization Discussion

The solution has a subtle optimization:
```python
if node.val == subRoot.val:
    is_subtree = self.isSameTree(node, subRoot)
```

By checking value equality first, you avoid calling `isSameTree` when values don't match. However, this could be simplified:

```python
# Always check, let isSameTree handle the value comparison
if self.isSameTree(node, subRoot):
    return True
return dfs(node.left) or dfs(node.right)
```

Both approaches work, but yours potentially saves function calls.

## Key Insights

1. **Composition pattern** - Complex problems often build on simpler ones

2. **Search continuation** - Don't stop at first potential match

3. **OR propagation** - First True in OR chain determines result

4. **Value as filter** - Checking values first can optimize tree comparisons

5. **Recursive simplicity** - The main function is remarkably concise

## What I Learned

The solution effectively demonstrates problem composition - using `isSameTree` as a black box to solve a more complex problem. The critical insight is continuing the search even after a failed match when values are equal, because the actual subtree might be deeper. The OR chain cleanly handles the "found anywhere" requirement. This pattern of building on previous solutions is common in tree problems and shows good problem-solving methodology.