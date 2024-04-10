# Attempt 1: O(n) efficient solution

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(None, head)
        prev = head
        curr = head.next

        repeat = False
        while curr:
            if curr.next and (curr.val == curr.next.val):
                repeat = True
            elif repeat:
                prev.next = curr.next
                repeat = False
            else:
                prev = curr

            curr = curr.next

        return head.next

