# Attemp 1: Fitst attempt with naive approach

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

        tail = fast
        k = k % n
        k = n - k
        slow = head
        for idx in range(1, k):
            slow = slow.next

        tail.next = head
        head = slow.next
        slow.next = None
        
        return head

