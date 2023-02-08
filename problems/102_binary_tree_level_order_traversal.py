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

