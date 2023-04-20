# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.left_widths = []
        self.right_widths = []
        def helper(node, dir, width):
            if node is None:
                return
            if dir == "left":
                self.left_widths.append(width)
                if node.left:
                    helper(node.left, dir, width*2)
                else:
                    helper(node.right, dir, (width*2-1))
            if dir == "right":
                self.right_widths.append(width)
                if node.right:
                    helper(node.right, dir, width*2)
                else:
                    helper(node.left, dir, (width*2-1))

        helper(root, "left", 1)
        helper(root, "right", 1)

        last_common_level = min(len(self.left_widths), len(self.right_widths))

        max_width = 0
        for i in range(last_common_level):
            minus = (2**(i) - self.left_widths[i]) + (2**(i) - self.right_widths[i])
            width = (2**(i)) - minus
            if width > max_width:
                max_width = width
        
        return max_width

