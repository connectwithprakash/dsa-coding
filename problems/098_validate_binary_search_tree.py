# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inOrderTraversal(self, root, prev_val, prev_is_valid):
        if not prev_is_valid:
            return prev_val, prev_is_valid
        if root.left:
            prev_val, left_is_valid = self.inOrderTraversal(root.left, prev_val, prev_is_valid)
            prev_is_valid = prev_is_valid & left_is_valid
        if root.val > prev_val:
            prev_val = root.val
            prev_is_valid = (prev_is_valid & True)
        else:
            prev_is_valid = (prev_is_valid & False)
        if root.right:
            prev_val, right_is_valid = self.inOrderTraversal(root.right, prev_val, prev_is_valid)
            prev_is_valid = prev_is_valid & right_is_valid

        return prev_val, prev_is_valid

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev_val = -2e31
        prev_val, is_valid_vst = self.inOrderTraversal(root, prev_val, True)
        
        return is_valid_vst

