# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Recursive solution
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def recursion(node: Optional[ListNode]) -> None:
            if (node is not None) and (node.next is not None):
                node.val, node.next.val = node.next.val, node.val
                recursion(node.next.next)
        
        recursion(head)
        return head
        
