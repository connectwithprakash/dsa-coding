# Binary Tree Maximum Path Sum

## Problem
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

## My Approach

I realized that at each node, the maximum path sum could be:
1. Just the node itself
2. Node + left subtree path
3. Node + right subtree path  
4. Left subtree path + node + right subtree path (path through node)

However, when returning to parent, I can only return paths that extend upward (options 1-3), not the path through the node (option 4).

## Solution with Comments

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Track global maximum across all paths
        self._max_path_sum = -float("inf")
        
        def dfs(root):
            if not root:
                return 0
            
            # Get max path sums from subtrees
            left_path_sum = dfs(root.left)
            right_path_sum = dfs(root.right)
            
            # Update global max considering all possible paths through this node
            self._max_path_sum = max(
                self._max_path_sum,
                root.val,                              # Just node
                left_path_sum + root.val,              # Left + node
                right_path_sum + root.val,             # Right + node
                left_path_sum + root.val + right_path_sum  # Left + node + right
            )
            
            # Return max path that can extend upward to parent
            # Cannot include both left and right (that would be a complete path)
            return max(root.val, 
                      root.val + left_path_sum, 
                      root.val + right_path_sum)
        
        dfs(root)
        return self._max_path_sum
```

**Note:** This solution is complete and handles negative values correctly. By considering all possibilities in the max() function (including just `root.val` alone), it naturally handles cases where including negative subtree paths would reduce the sum.

## Alternative Solution (Explicit Negative Filtering)

```python
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self._max_path_sum = float('-inf')
        
        def dfs(node):
            if not node:
                return 0
            
            # Only take positive contributions from subtrees
            # If a subtree path sum is negative, ignore it (use 0)
            left_gain = max(dfs(node.left), 0)
            right_gain = max(dfs(node.right), 0)
            
            # Path through current node (can't extend further up)
            current_max = node.val + left_gain + right_gain
            
            # Update global maximum
            self._max_path_sum = max(self._max_path_sum, current_max)
            
            # Return max gain if we continue path through parent
            return node.val + max(left_gain, right_gain)
        
        dfs(root)
        return self._max_path_sum
```

This alternative approach explicitly filters out negative contributions by using `max(..., 0)`. It's more concise but functionally equivalent to the original solution. Both handle all edge cases correctly.

## Visual Intuition

### Example 1: Path Through Root

```
       -10
       /  \
      9    20
          /  \
         15   7

Possible paths at node 20:
- Just 20: sum = 20
- 20 + 15: sum = 35
- 20 + 7: sum = 27
- 15 + 20 + 7: sum = 42 ✓ (max at this node)
Return to parent: max(20, 35, 27) = 35

At root -10:
- Just -10: sum = -10
- -10 + 9: sum = -1
- -10 + 35: sum = 25
- 9 + -10 + 35: sum = 34

Global max = 42 (path: 15→20→7)
```

### Example 2: Single Node Path

```
       2
      / \
    -1  -2

At left child: max = -1, return -1
At right child: max = -2, return -2
At root:
- Just 2: sum = 2 ✓
- 2 + (-1): sum = 1
- 2 + (-2): sum = 0
- (-1) + 2 + (-2): sum = -1

Global max = 2 (just the root)
```

### Key Insight Visualization

```
At each node, we consider two different things:

1. What's the maximum path sum using this node?
   (Could be left→node→right)
   
2. What's the maximum we can contribute upward?
   (Must be a single path: node, node→left, or node→right)

        node
        /  \
     left  right
     
Max through node: left + node + right (stays local)
Max to return: max(node, node+left, node+right) (extends up)
```

## Why This Works

The algorithm works by:
1. **Post-order traversal**: Process children before parent to get their contributions
2. **Global tracking**: Keep track of the best path sum seen anywhere
3. **Return constraint**: Return only paths that can extend upward
4. **Negative handling**: Include negative values when they're part of nodes, but can choose to exclude negative path contributions

The separation between what we track globally (any path) and what we return (extendable path) is the key insight.

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
# Edge Case 1: Single node (negative)
root = TreeNode(-3)
# Result: -3 (must include at least one node)

# Edge Case 2: All negative values
#      -2
#      / \
#    -1  -3
# Result: -1 (best single node)

# Edge Case 3: Path doesn't include root
#       1
#      / \
#     2   3
#    / \
#   4   5
# Best path might be 4→2→5 (sum=11) not through root

# Edge Case 4: Straight line (all positive)
#     1
#      \
#       2
#        \
#         3
# Result: 6 (entire path)

# Edge Case 5: Negative root, positive children
#      -3
#      / \
#     9   20
# Result: 26 (9→-3→20 is worse than just 9 or 20 alone)
```

## Common Mistakes

1. **Forgetting to handle negative values**:
   ```python
   # Wrong: Forces inclusion of negative paths
   return root.val + left_path_sum + right_path_sum
   
   # Correct: Can choose to exclude negative contributions
   left_gain = max(dfs(node.left), 0)
   ```

2. **Returning the path through node**:
   ```python
   # Wrong: Returns left+node+right to parent
   return left_path_sum + root.val + right_path_sum
   
   # Correct: Parent can only use one branch
   return max(root.val, root.val + left_path_sum, root.val + right_path_sum)
   ```

3. **Not initializing to negative infinity**:
   ```python
   # Wrong: Assumes at least one positive value exists
   self._max_path_sum = 0
   
   # Correct: Handles all negative trees
   self._max_path_sum = float('-inf')
   ```

## Pattern Recognition

This problem demonstrates:
- **Global vs local optimization** - Track global max while returning local contribution
- **Path constraints** - Understanding what constitutes a valid path
- **Negative value handling** - Choosing when to include/exclude paths
- **Tree DP pattern** - Using subtree results to compute parent result

Similar problems:
- Binary Tree Maximum Path Product
- Diameter of Binary Tree (path length instead of sum)
- House Robber III (can't use adjacent nodes)
- Path Sum III (paths with target sum)

## Key Insights

1. **Two different values** - What to track globally vs what to return to parent

2. **Path definition** - A path can't branch at a node when extending upward

3. **Negative paths** - Can choose not to include negative contributing paths

4. **Must include something** - Even if all negative, must include at least one node

5. **Post-order traversal** - Need subtree information before processing node

## What I Learned

The solution demonstrates the important pattern of tracking different values during tree traversal. The global maximum can be any valid path in the tree, but what we return must be a path that can extend upward. This separation is crucial - at each node we consider all possible paths through it for the global maximum, but only return the best single branch to the parent. The handling of negative values adds complexity but follows the principle that we must include nodes but can choose to exclude paths.