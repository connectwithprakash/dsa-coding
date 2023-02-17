# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def inorder(node, sorted_arr):
            if node.left:
                inorder(node.left, sorted_arr)
            sorted_arr.append(node.val)
            if node.right:
                inorder(node.right, sorted_arr)

            return sorted_arr

        sorted_arr = inorder(root, [])
        min_distance = float("inf")
        
        for j in range(1, len(sorted_arr)):
            local_min = (sorted_arr[j] - sorted_arr[j-1])
            if local_min < min_distance:
                min_distance = local_min

        return min_distance

