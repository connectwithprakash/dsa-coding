# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Another minimal code solution:
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if node is None:
            return 0

        return 1+max(self.maxDepthhelper(root.left), self.maxDepth(root.right))
"""


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def helper(node, count):
            if node is None:
                return count
            
            left_depth = helper(node.left, count+1)
            right_depth = helper(node.right, count+1)

            return max(left_depth, right_depth)
        
        return helper(root, 0)

