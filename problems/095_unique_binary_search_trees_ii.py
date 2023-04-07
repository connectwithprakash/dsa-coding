# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def helper(p, q):
            if p > q:
                return [None]
            
            trees = []
            for i in range(p, q+1):
                root = TreeNode(i)
                for left_tree in helper(p, i-1):
                    for right_tree in helper(i+1, q):
                        root.left = left_tree
                        root.right = right_tree
                        trees.append(root)
            return trees
        
        return helper(1, n)

