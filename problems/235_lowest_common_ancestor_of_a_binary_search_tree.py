# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def find_smaller_node(self, root: 'TreeNode', node: 'TreeNode') -> List['TreeNode']:
        parents = []
        if root is node:
            parents.append(root)
        else:
            if root.left:
                left = self.find_smaller_node(root.left, node)
                parents += left
            if root.right:
                if node not in parents:
                    right = self.find_smaller_node(root.right, node)
                    parents += right
            if node in parents:
                    parents.append(root)
        return parents


    def find_bigger_node(self, root: 'TreeNode', node: 'TreeNode', parents: List['TreeNode']) -> 'TreeNode':
        node_found = False
        common_ancestor = None
        if (root is node):
            common_ancestor = root
            node_found = True
        else:
            if root.left:
                node_found, left = self.find_bigger_node(root.left, node, parents)
                if node_found:
                    if left in parents:
                        common_ancestor = left
                    elif root in parents:
                        common_ancestor = root
            if (root.right is not None) & (not node_found):
                if not node_found:
                    node_found, right = self.find_bigger_node(root.right, node, parents)
                if node_found & (common_ancestor is None):
                    if right in parents:
                        common_ancestor = right
                    elif root in parents:
                        common_ancestor = root

        return node_found, common_ancestor
                
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val < q.val:
            smaller_node = p
            bigger_node = q
        else:
            smaller_node = q
            bigger_node = p

        parents_of_smaller_node = self.find_smaller_node(root, smaller_node)
        _, lowest_common_ancestor = self.find_bigger_node(root, bigger_node, parents_of_smaller_node)
        return lowest_common_ancestor

