# Intuition
First I thought of doing a recursive search but saw the suggestion to find an iterative solution. Then, I thought of using queue for traversal but there is no inbuilt queue without collections import. So, I created a proxy of queue from list's native pop, reverse, and extend operations.

# Approach
Firstly, I check if the root node exist or not. If the root node exists, I add it to the frontier (children list). Then, I loop through the frontier by poping the last node looking for children for each nodes. If the node has children, I reverse the order of the children and add them to the frontier so that when I pop, I get children from left to right. After putting childrens to the frontier, I add the root to the preorder list. 

# Complexity
- Time complexity: $$O(n)$$

- Space complexity: $$O(n)$$


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

