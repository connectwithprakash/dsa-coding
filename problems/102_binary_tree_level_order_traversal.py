"""
# Intuition
The idea is to create a frontier that acts as a queue for BFS. From the frontier some how extract the elements that are on the same level. For that we try to find where the first node at a level is and the last node is denoted by start and end indices. We then use these indices to extract the node value iterating through these indices.

# Approach
We first instantiate frontier with the root node, start with 0 and end with length of the frontier.
1. Check if the start and end indices are same.
2. Loop through the elements given by start and end-1 indices and add them to level nodes list and look for its children and add them to frontier.
3. Update the start index with end index and end index with length of updated frontier.
4. Repeat step 1 to 3.

# Complexity
- Time complexity: $$O(n)$$

- Space complexity: $$O(n)$$
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            level_order_traversal = []
        else:
            frontier = [root]
            start = 0
            end = len(frontier)
            level_order_traversal = []
            while start != end:
                level_items = []
                for node in frontier[start:end]:
                    level_items.append(node.val)
                    if node.left is not None:
                        frontier.append(node.left)
                    if node.right is not None:
                        frontier.append(node.right)
                level_order_traversal.append(level_items)
                start = end
                end = len(frontier)

        return level_order_traversal

