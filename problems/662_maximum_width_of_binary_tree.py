# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Level order traversal using BFS to get width at each level
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Create a queue with node and index
        queue = [(root, 0)]
        level_queue = queue
        max_width = 1
        while queue:
            level_queue = []
            # Loop through each node in the level frontier to get its child
            for node, i in queue:
                if node.left:
                    level_queue.append((node.left, 2*i+1))
                if node.right:
                    level_queue.append((node.right, 2*i+2))
            # Check the max width at the current level
            if level_queue:
                # We subtract the index of right most and the left most child
                # of that level to get level width
                level_width = level_queue[-1][1] - level_queue[0][1] + 1
                if level_width > max_width:
                    max_width = level_width
            # Replace the queue with child of next level
            queue = level_queue

        return max_width

