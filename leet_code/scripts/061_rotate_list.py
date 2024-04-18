# Attemp 1: Fitst attempt with 0(n) using fast pointer

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        fast = head.next

        n = 2
        while fast.next: 
            if fast.next.next is None:
                fast = fast.next
                n += 1
            else:
                fast = fast.next.next
                n += 2

        # connect tail to head
        fast.next = head
        
        k = k % n
        k = n - k
        fast = head

        idx = 1
        while (idx+2) <= k:
            fast = fast.next.next
            idx += 2
        
        if idx != k:
            fast = fast.next

        head = fast.next
        fast.next = None
        
        return head

