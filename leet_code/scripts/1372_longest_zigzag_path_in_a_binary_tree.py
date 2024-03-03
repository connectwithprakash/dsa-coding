# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Brute-force solution
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
	# Go ZigZag traversal
        def helper(node, direction):
            print(node.val, direction)
            if node.right and (direction == "left"):
                return 1 + helper(node.right, "right")
            elif node.left and (direction == "right"):
                return 1 + helper(node.left, "left")
            else:
                return 1
	# DFS
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


# Efficient O(n) solution
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.max_path_len = 0

        def traversal(node, dir, path_len):
            self.max_path_len = max(self.max_path_len, path_len)
            
            if node.left is not None:
                if dir != "left":
                    traversal(node.left, "left", path_len+1)
                else:
                    traversal(node.left, "left", 1)

            if node.right is not None:
                if dir != "right":
                    traversal(node.right, "right", path_len+1)
                else:
                    traversal(node.right, "right", 1)

        traversal(root, "root", 0)

        return self.max_path_len

