# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue = [(root, 0)]
        level_queue = queue
        max_width = 1
        while queue:
            level_queue = []
            for node, i in queue:
                if node.left:
                    level_queue.append((node.left, 2*i+1))
                if node.right:
                    level_queue.append((node.right, 2*i+2))
            
            if level_queue:
                level_width = level_queue[-1][1] - level_queue[0][1] + 1
                if level_width > max_width:
                    max_width = level_width

            queue = level_queue

        return max_width

