# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inOrderTraversal(self, node, low_limit, high_limit):
        if node is None:
            return True
        elif (low_limit < node.val < high_limit):
            left_is_valid = self.inOrderTraversal(node.left, low_limit, node.val)
            right_is_valid = self.inOrderTraversal(node.right, node.val, high_limit)
            
            return left_is_valid and right_is_valid
        else:
            return False

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.inOrderTraversal(root, -float("inf"), float("inf"))

