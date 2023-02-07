# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root:
            children = [root]
        else:
            children = []
        preorder_elements = []
        while children:
            node = children.pop()
            if len(node.children):
                children.extend(node.children[::-1])
            
            preorder_elements.append(node.val)
        return preorder_elements

