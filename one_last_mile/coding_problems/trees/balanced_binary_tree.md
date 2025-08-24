# Balanced Binary Tree

## Problem
Given a binary tree, determine if it is height-balanced.

A height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differs by more than one.

## My Approach

I used the same pattern as the diameter problem - computing heights while tracking a global condition. As I calculate the height of each subtree, I check if the difference exceeds 1. If any node is unbalanced, I set a flag to False. This single-pass approach is efficient and clean.

## Solution with Comments

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Track if tree is balanced globally
        self._is_balanced = True
        
        def dfs(node):
            # Base case: empty tree has height 0
            if node is None:
                return 0
            
            # Get heights of left and right subtrees
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            
            # Check balance condition at this node
            if abs(left_height - right_height) > 1:
                self._is_balanced = False
            
            # Return height for parent's calculation
            return max(left_height, right_height) + 1
        
        dfs(root)
        return self._is_balanced
```

## Alternative Solution - Early Termination

```python
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            # Base case
            if not node:
                return 0
            
            # Get left height, -1 indicates unbalanced
            left_height = dfs(node.left)
            if left_height == -1:
                return -1
            
            # Get right height
            right_height = dfs(node.right)
            if right_height == -1:
                return -1
            
            # Check balance at current node
            if abs(left_height - right_height) > 1:
                return -1
            
            # Return height if balanced
            return max(left_height, right_height) + 1
        
        return dfs(root) != -1
```

## Visual Intuition

### Example 1: Balanced Tree

```
        3
       / \
      9   20
         /  \
        15   7

Heights:
- Node 9: height = 0
- Node 15: height = 0
- Node 7: height = 0
- Node 20: height = 1, |left(0) - right(0)| = 0 ✓
- Node 3: height = 2, |left(0) - right(1)| = 1 ✓

Result: Balanced
```

### Example 2: Unbalanced Tree

```
        1
       / \
      2   2
     / \
    3   3
   / \
  4   4

Heights and Balance Checks:
- Nodes 4: height = 0
- Nodes 3: height = 1, |1 - 1| = 0 ✓
- Left 2: height = 2, |2 - 0| = 2 ✗ (UNBALANCED!)
- Right 2: height = 0
- Root 1: height = 3, |3 - 0| = 3 ✗

Result: Unbalanced (fails at node 2)
```

### Key Insight Visualization

```
At each node:
     node
     /  \
   left  right
   
Balance check: |left_height - right_height| ≤ 1
Height: 1 + max(left_height, right_height)

Global tracking: If ANY node fails, entire tree is unbalanced
```

## Why This Works

The solution brilliantly reuses the pattern from the diameter problem:
1. **Height computation** - Needed for parent nodes
2. **Balance tracking** - Global flag to track if any subtree is unbalanced
3. **Single traversal** - Check all nodes in one pass

The key insight is that we must check balance at EVERY node, not just the root. A single unbalanced node makes the entire tree unbalanced.

## Complexity Analysis

### Your Solution
- **Time Complexity:** O(n)
  - Visit each node exactly once
  - O(1) work per node
- **Space Complexity:** O(h)
  - Recursion stack depth
  - Best case (balanced): O(log n)
  - Worst case (skewed): O(n)

### Early Termination Solution
- **Time Complexity:** O(n) worst case, but can terminate early
- **Space Complexity:** O(h)

## Edge Cases

```python
# Edge Case 1: Empty tree
root = None
# Result: True (empty tree is balanced)

# Edge Case 2: Single node
root = TreeNode(1)
# Result: True

# Edge Case 3: Linear chain (skewed)
#     1
#      \
#       2
#        \
#         3
# Result: False (height difference = 2)

# Edge Case 4: Perfect binary tree
#       1
#      / \
#     2   3
#    / \ / \
#   4  5 6  7
# Result: True (all nodes balanced)

# Edge Case 5: Subtree unbalanced
#       1
#      / \
#     2   3
#    /
#   4
#  /
# 5
# Result: False (node 2 has imbalance)
```

## Common Mistakes

1. **Only checking root balance**:
   ```python
   # Wrong: Only checks if root's children are balanced
   left_height = getHeight(root.left)
   right_height = getHeight(root.right)
   return abs(left_height - right_height) <= 1
   
   # Correct: Must check EVERY node
   ```

2. **Not tracking global state properly**:
   ```python
   # Wrong: Local variable doesn't persist
   is_balanced = True  # This resets each call!
   
   # Correct: Use instance variable or return special value
   self._is_balanced = True
   ```

3. **Confusing height with depth**:
   ```python
   # Wrong: Using depth instead of height
   return 1 + min(left_height, right_height)
   
   # Correct: Height uses max
   return 1 + max(left_height, right_height)
   ```

## Pattern Recognition

This problem demonstrates:
- **Global condition tracking** - Using class variable to track tree-wide property
- **Height computation with side effects** - Calculate one value while checking another
- **Bottom-up validation** - Check subtrees before parent

Similar problems:
- Diameter of Binary Tree (same pattern!)
- Validate Binary Search Tree (track validity while traversing)
- Maximum Path Sum (track max while computing paths)
- Symmetric Tree (check property at each level)

## Optimization Discussion

This solution always traverses the entire tree. The alternative with early termination can stop as soon as imbalance is found:

```python
# This approach: Always O(n)
- Continues even after finding imbalance
- Simpler code, consistent performance

# Early termination: Best case O(1), worst case O(n)
- Returns immediately on imbalance
- More complex but potentially faster
```

For interview settings, your approach is excellent - clean, easy to understand, and follows a familiar pattern.

## Key Insights

1. **Pattern reuse** - Same structure as diameter problem shows pattern mastery

2. **Global vs local** - Tree balance is a global property determined by all nodes

3. **Height vs balance** - Computing height enables balance checking

4. **Single pass sufficiency** - No need for separate height and balance passes

5. **Bottom-up nature** - Must know subtree heights before checking current node

## What I Learned

The solution shows excellent pattern recognition - immediately seeing the similarity to the diameter problem and applying the same technique. The pattern of computing one value (height) while tracking another condition (balance) is powerful and appears frequently. Using a class variable for the global state is cleaner than the -1 sentinel approach, though the latter can terminate early. This problem reinforces that tree properties often require checking every node, not just the root.