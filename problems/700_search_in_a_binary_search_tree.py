# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# First Attempt: Brute-force
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if (root.val == val):
            return root
        else:
            sub_tree = None
            if root.left:
                sub_tree = self.searchBST(root.left, val)
            if (sub_tree is None) and (root.right):
                sub_tree = self.searchBST(root.right, val)
        
            return sub_tree

# Second attempt: nlong(n) solution
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        sub_tree = None
        if root:
            if (root.val == val):
                sub_tree = root
            elif (val < root.val):
                sub_tree = self.searchBST(root.left, val)
            elif (val > root.val):
                sub_tree = self.searchBST(root.right, val)
        
        return sub_tree

