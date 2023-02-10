# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def find_path(self, root: 'TreeNode', node: 'TreeNode') -> List['TreeNode']:
        path = []
        if root is node:
            path.append(root)
        else:
            if root.left:
                left = self.find_path(root.left, node)
                path += left
            if root.right:
                if node not in path:
                    right = self.find_path(root.right, node)
                    path += right
            if node in path:
                    path.append(root)
        return path
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_paths = self.find_path(root, p)
        q_paths = self.find_path(root, q)
        if len(p_paths) > len(q_paths):
            for node in p_paths:
                if node in q_paths:
                    return node
        else:
            for node in q_paths:
                if node in p_paths:
                    return node

