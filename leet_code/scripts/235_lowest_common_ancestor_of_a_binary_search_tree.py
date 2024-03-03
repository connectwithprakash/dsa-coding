# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution: 
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    # After reading about LCA from wikipedia and using algorithm for range minimum query (RMQ.
        if (root.val < p.val) & (root.val < q.val):
            return self.lowestCommonAncestor(root.right, p, q)
        elif (root.val > p.val) & (root.val > q.val):
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root

