# Attemp 1: Fitst attempt with 0(n) using fast pointer

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Check if the list is empty or has only one node
        if head is None or head.next is None:
            return head

        # Find the length of the list and locate the last node
        fast = head.next
        n = 2
        while fast.next: 
            if fast.next.next is None:
                fast = fast.next
                n += 1
            else:
                fast = fast.next.next
                n += 2

        # Connect the last node to the head to form a cycle
        fast.next = head
        
        # Calculate the actual rotation amount
        k = k % n
        # Calculate the number of steps to reach the new head after rotation
        k = n - k
        fast = head

        idx = 1
        # Move the 'fast' pointer to the node before the new head
        while (idx+2) <= k:
            fast = fast.next.next
            idx += 2
        
        # If there are odd number of steps to the new head, move 'fast' pointer one more step
        if idx != k:
            fast = fast.next

        # Set the new head and break the cycle to form the rotated list
        head = fast.next
        fast.next = None
        
        return head

