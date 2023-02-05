# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        while head is not None:
            if head.val is not None:
                head.val = None
                head = head.next
            else:
                break

        return head
