# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# O(n/2) for search of length of linked list and O(n) for removal.
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        slow = None
        sz = 0
        idx = 0
        while fast:
            if fast.next:
                fast = fast.next.next
                sz += 2
            else:
                fast = fast.next
                sz += 1
        
        for idx in range(sz-n):
            if idx == 0:
                slow = head
            else:
                slow = slow.next
        
        if slow is None or (sz-n) == 0:
            head = head.next
        else:
            slow.next = slow.next.next
        
        return head


# O(n/2) for length of linked list and (n/2) to search for node to delete.
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        slow = None
        sz = 0
        while fast:
            if fast.next:
                fast = fast.next.next
                sz += 2
            else:
                fast = fast.next
                sz += 1
        
        if (sz-n) == 0:
            head = head.next
        else:
            idx = 1
            fast = head
            while (idx+2) <= (sz-n):
                fast = fast.next.next
                idx += 2
            if idx == (sz-n):
                fast.next = fast.next.next
            else:
                fast.next.next = fast.next.next.next

        return head

