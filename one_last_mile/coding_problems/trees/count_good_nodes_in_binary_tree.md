# Count Good Nodes in Binary Tree

## Problem
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

## My Approach

I track the maximum value seen along the path from root to current node. If the current node's value is greater than or equal to this maximum, it's a good node. I update the maximum for the recursive calls to children.

## Solution with Comments

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        
        def dfs(node, max_val):
            if not node:
                return
            
            # Update max value seen so far on this path
            max_val = max(node.val, max_val)
            
            # If current node >= max, it's a good node
            if node.val >= max_val:
                self.count += 1
            
            # Traverse children with updated max
            if node.left:
                dfs(node.left, max_val)
            if node.right:
                dfs(node.right, max_val)
        
        # Start with -inf since node values can be negative
        # Problem constraint: -10^4 <= Node.val <= 10^4
        dfs(root, float('-inf'))
        
        return self.count
```

## Alternative Solution - Return Count

```python
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_so_far):
            if not node:
                return 0
            
            # Count this node if it's good
            good_count = 1 if node.val >= max_so_far else 0
            
            # Update max for children
            max_so_far = max(max_so_far, node.val)
            
            # Add counts from subtrees
            good_count += dfs(node.left, max_so_far)
            good_count += dfs(node.right, max_so_far)
            
            return good_count
        
        return dfs(root, float('-inf'))
```

## Visual Intuition

### Example Tree

```
        3           Good nodes: 3, 4, 5, 3
       / \          
      1   4         Path to 1: [3, 1] → max=3, 1<3 → Not good
     /   / \        Path to 3: [3, 1, 3] → max=3, 3>=3 → Good
    3   1   5       Path to 4: [3, 4] → max=4, 4>=4 → Good
                    Path to 1: [3, 4, 1] → max=4, 1<4 → Not good
                    Path to 5: [3, 4, 5] → max=5, 5>=5 → Good
```

### Step-by-Step Trace

```
Call: dfs(3, -∞)
  max_val = max(3, -∞) = 3
  3 >= 3 → count = 1 ✓
  
  Call: dfs(1, 3)
    max_val = max(1, 3) = 3
    1 >= 3 → False
    
    Call: dfs(3, 3)
      max_val = max(3, 3) = 3
      3 >= 3 → count = 2 ✓
  
  Call: dfs(4, 3)
    max_val = max(4, 3) = 4
    4 >= 4 → count = 3 ✓
    
    Call: dfs(1, 4)
      max_val = max(1, 4) = 4
      1 >= 4 → False
    
    Call: dfs(5, 4)
      max_val = max(5, 4) = 5
      5 >= 5 → count = 4 ✓

Total: 4 good nodes
```

## Why This Works

The algorithm works because:
1. **Path maximum tracking**: We maintain the maximum value from root to current node
2. **Update before check**: Updating max first simplifies the logic - if current node is the new max, it's automatically good
3. **Independent paths**: Each path from root is evaluated independently

The smart part is that after `max_val = max(node.val, max_val)`:
- If `node.val` was already less than `max_val`, it remains less (not good)
- If `node.val` was greater or equal, it becomes the new max and equals it (good)

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
root = TreeNode(5)
# Result: 1 (root is always good)

# Edge Case 2: All increasing path
#     1
#      \
#       2
#        \
#         3
# Result: 3 (all nodes are good)

# Edge Case 3: All decreasing path
#     3
#    /
#   2
#  /
# 1
# Result: 1 (only root is good)

# Edge Case 4: Negative values
#     -3
#    /  \
#   -4   -2
# Result: 2 (root -3 and right child -2)

# Edge Case 5: Same values
#     5
#    / \
#   5   5
# Result: 3 (all are good, >= includes equality)
```

## Common Mistakes

1. **Wrong initial max value**:
   ```python
   # Wrong: Assumes all values are positive
   dfs(root, 0)
   
   # Correct: Use -inf or problem's minimum constraint
   dfs(root, float('-inf'))
   ```

2. **Checking before updating max**:
   ```python
   # Alternative approach (also valid):
   if node.val >= max_val:
       self.count += 1
   max_val = max(node.val, max_val)  # Update after
   ```

3. **Not handling equality**:
   ```python
   # Wrong: Misses nodes equal to max
   if node.val > max_val:
   
   # Correct: >= includes equal values
   if node.val >= max_val:
   ```

## Pattern Recognition

This problem demonstrates:
- **Path tracking** - Maintaining state along root-to-node paths
- **Maximum tracking** - Common pattern in tree traversal
- **Good/bad node classification** - Binary classification during traversal

Similar problems:
- Path Sum (track sum instead of max)
- Binary Tree Maximum Path Sum
- Count Univalue Subtrees
- Path with Maximum Average

## Key Insights

1. **Root is always good** - No nodes above it to compare

2. **Path independence** - Each root-to-leaf path is evaluated independently

3. **Update-then-check elegance** - Simplifies the good node condition

4. **Single pass sufficiency** - No need to traverse twice

5. **State passing** - DFS naturally maintains path state

## What I Learned

The solution effectively tracks the path maximum using DFS parameter passing. The insight that updating max before checking simplifies the logic is thoughtful - it unifies the "equals max" and "exceeds max" cases. This pattern of maintaining path-specific state through recursion parameters is common in tree problems and avoids the need for backtracking or path arrays.