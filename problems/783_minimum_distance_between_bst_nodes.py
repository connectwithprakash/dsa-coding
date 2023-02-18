# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    min_distance = float("inf")
    prev_val = - float("inf")

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        if not root:
            return
        self.minDiffInBST(root.left)
        if (root.val - self.prev_val) < self.min_distance:
            self.min_distance = (root.val - self.prev_val)
        self.prev_val = root.val
        self.minDiffInBST(root.right)
        
        return self.min_distance

