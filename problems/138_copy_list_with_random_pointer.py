# Attempt 1: My approach without hints - gives better result
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
            
        temp = head
        results = []

        # Create a copy of the nodes
        idx = 0
        while temp:
            results.append(Node(temp.val, None, temp.random))
            temp.val = idx
            idx += 1
            temp = temp.next

        # Link node with the next node
        for idx in range(len(results)-1):
            results[idx].next = results[idx+1]

        # Set random link to approprite node from the new list
        for node in results:
            node.random = results[node.random.val] if node.random else None

        results = results[0]

        # Revert the value of original linkedlist
        temp1, temp2 = head, results
        while temp1 and temp2:
            temp1.val = temp2.val
            temp1 = temp1.next
            temp2 = temp2.next

        return results


# Second Attempt
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        new_head = Node(0)

        oldlist2newlist = {}

        # Create a list with new nodes
        temp1, temp2 = new_head, head
        while temp2:
            temp1.next = Node(temp2.val, None, temp2.random)
            temp1 = temp1.next
            oldlist2newlist[temp2] = temp1
            temp2 = temp2.next

        new_head = new_head.next

        # Replace the random node link from old to new
        temp1 = new_head
        while temp1:
            temp1.random = oldlist2newlist[temp1.random] if temp1.random else None
            temp1 = temp1.next

        del oldlist2newlist

        return new_head

