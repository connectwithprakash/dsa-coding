# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Brute-force solution
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def helper(node, direction):
            print(node.val, direction)
            if node.right and (direction == "left"):
                return 1 + helper(node.right, "right")
            elif node.left and (direction == "right"):
                return 1 + helper(node.left, "left")
            else:
                return 1

        def traversal(node, direction):
            ll_path, lr_path, mid_path = 0, 0, 0
            if node.left:
                ll_path = traversal(node.left, "left")
            if node.right:
                lr_path = traversal(node.right, "right")
            if direction != "root":
                mid_path = helper(node, direction)
            return max(mid_path, ll_path, lr_path)

        return traversal(root, "root")

