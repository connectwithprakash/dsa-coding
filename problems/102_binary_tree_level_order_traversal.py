# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        else:
            # Here 1 denotes the start while 2 denotes the stop of the level nodes in the frontier
            frontier = [1, root, 2]
            level_order_traversal = []
            index = 0
            while index != len(frontier):
                if (frontier[index] == 1):
                    if (frontier[index+1] != 2):
                        level_items = []
                        frontier.append(1)
                    else:
                        break
                elif (frontier[index] == 2):
                    level_order_traversal.append(level_items)
                    frontier.append(2)
                else:
                    level_items.append(frontier[index].val)
                    if frontier[index].left is not None:
                        frontier.append(frontier[index].left)
                    if frontier[index].right is not None:
                        frontier.append(frontier[index].right)
                index += 1
            return level_order_traversal

