# Construct Binary Tree from Preorder and Inorder Traversal

## Problem
Given two integer arrays `preorder` and `inorder` where `preorder` is the preorder traversal of a binary tree and `inorder` is the inorder traversal of the same tree, construct and return the binary tree.

## My Approach

I use the fact that in preorder, the first element is always the root. In inorder, this root element divides the array into left subtree (elements before root) and right subtree (elements after root). The count of elements in the left subtree from inorder tells me how many elements from preorder belong to the left subtree.

## Solution with Comments

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        # First element in preorder is always the root
        root = TreeNode(preorder[0])
        
        # Find root's position in inorder to split left/right
        mid_idx = inorder.index(root.val)
        
        # Left subtree: 
        # - preorder: skip root, take 'mid_idx' elements
        # - inorder: take all elements before root
        root.left = self.buildTree(preorder[1:mid_idx + 1], inorder[:mid_idx])
        
        # Right subtree:
        # - preorder: skip root and left subtree elements
        # - inorder: take all elements after root
        root.right = self.buildTree(preorder[mid_idx + 1:], inorder[mid_idx + 1:])
        
        return root
```

## Optimized Solution with Index Tracking

```python
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Build hashmap for O(1) index lookup in inorder
        inorder_map = {val: i for i, val in enumerate(inorder)}
        self.preorder_idx = 0
        
        def build(in_start, in_end):
            if in_start > in_end:
                return None
            
            # Pick current root from preorder
            root_val = preorder[self.preorder_idx]
            root = TreeNode(root_val)
            self.preorder_idx += 1
            
            # Root splits inorder list into left and right subtrees
            inorder_idx = inorder_map[root_val]
            
            # Build left subtree first (preorder: root -> left -> right)
            root.left = build(in_start, inorder_idx - 1)
            # Then build right subtree
            root.right = build(inorder_idx + 1, in_end)
            
            return root
        
        return build(0, len(inorder) - 1)
```

## Visual Intuition

### Example: Building Tree Step by Step

```
preorder = [3, 9, 20, 15, 7]
inorder  = [9, 3, 15, 20, 7]

Step 1: Root is 3 (first in preorder)
        3
       / \
      ?   ?
      
inorder: [9] | 3 | [15, 20, 7]
         left      right

Step 2: Left subtree
preorder for left: [9] (1 element, since left has 1 element)
inorder for left: [9]
        3
       /
      9

Step 3: Right subtree  
preorder for right: [20, 15, 7]
inorder for right: [15, 20, 7]
Root is 20, splits to [15] | 20 | [7]
        3
       / \
      9   20
         /  \
        15   7

Final tree constructed!
```

### Array Splitting Visualization

```
Original:
preorder: [A, B, D, E, C, F]
inorder:  [D, B, E, A, C, F]

Root A found at index 3 in inorder:
         
Left subtree (3 elements):          Right subtree (2 elements):
preorder: [B, D, E]                 preorder: [C, F]  
inorder:  [D, B, E]                 inorder:  [C, F]

This splitting continues recursively!
```

## Why This Works

The algorithm works because:
1. **Preorder property**: First element is always the root of current subtree
2. **Inorder property**: Root divides array into left and right subtrees
3. **Count preservation**: Number of left subtree elements in inorder = number to take from preorder
4. **Recursion**: Same pattern applies to all subtrees

The key insight is using inorder to determine subtree boundaries and applying those boundaries to preorder.

## Complexity Analysis

### Array Slicing Solution
- **Time Complexity:** O(n²)
  - n recursive calls (one per node)
  - Each call does O(n) work: `index()` is O(n), slicing is O(n)
  
- **Space Complexity:** O(n²)
  - Each recursion creates new array slices
  - Total space for all slices across recursion

### Optimized Index Solution  
- **Time Complexity:** O(n)
  - Build hashmap: O(n)
  - n recursive calls, each doing O(1) work
  
- **Space Complexity:** O(n)
  - Hashmap storage: O(n)
  - Recursion stack: O(h) where h is height
  - No array slicing overhead

## Edge Cases

```python
# Edge Case 1: Single node
preorder = [1], inorder = [1]
# Result: TreeNode(1)

# Edge Case 2: Skewed left tree
preorder = [3, 2, 1], inorder = [1, 2, 3]
#     3
#    /
#   2
#  /
# 1

# Edge Case 3: Skewed right tree
preorder = [1, 2, 3], inorder = [1, 2, 3]
# 1
#  \
#   2
#    \
#     3

# Edge Case 4: Complete binary tree
preorder = [1, 2, 4, 5, 3, 6, 7]
inorder = [4, 2, 5, 1, 6, 3, 7]
#       1
#      / \
#     2   3
#    / \ / \
#   4  5 6  7
```

## Common Mistakes

1. **Wrong preorder slicing**:
   ```python
   # Wrong: Off-by-one error
   root.left = self.buildTree(preorder[1:mid_idx], inorder[:mid_idx])
   
   # Correct: Include element at mid_idx
   root.left = self.buildTree(preorder[1:mid_idx + 1], inorder[:mid_idx])
   ```

2. **Using wrong traversal property**:
   ```python
   # Wrong: Thinking last element of preorder is root
   root = TreeNode(preorder[-1])  # That's postorder!
   
   # Correct: First element is root in preorder
   root = TreeNode(preorder[0])
   ```

3. **Not handling empty arrays**:
   ```python
   # Wrong: Will crash on empty array
   root = TreeNode(preorder[0])
   
   # Correct: Check first
   if not preorder or not inorder:
       return None
   ```

## Pattern Recognition

This problem demonstrates:
- **Divide and conquer** - Split problem into smaller subproblems
- **Tree construction** - Building tree from traversal sequences
- **Array partitioning** - Using one array to guide splitting of another
- **Recursion with different parameters** - Each call gets different array slices

Similar problems:
- Construct Binary Tree from Inorder and Postorder
- Serialize and Deserialize Binary Tree
- Verify Preorder Sequence in BST
- Construct BST from Preorder

## Key Insights

1. **Traversal uniqueness** - Preorder + inorder uniquely determine a tree (with unique values)

2. **Root identification** - Preorder gives roots in top-down order

3. **Subtree boundaries** - Inorder tells us where to split

4. **Count matching** - Left subtree size in inorder = elements to take from preorder

5. **Index optimization** - Hashmap eliminates repeated linear searches

## What I Learned

The solution demonstrates how different traversal orders encode complementary information about tree structure. Preorder tells us "what's the root?" while inorder tells us "what's on each side?". The array slicing approach is intuitive but creates O(n²) overhead. The optimized version using indices and a hashmap reduces this to O(n) by avoiding array copies and linear searches. This pattern of using one traversal to guide interpretation of another is fundamental to tree reconstruction problems.