# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        reverse = None
        slow = fast = head

        while (fast is not None) and (fast.next is not None):
            fast = fast.next.next

            temp = slow.next
            slow.next = reverse
            reverse = slow
            slow = temp

        if fast is not None:
            forward = slow.next
        else:
            forward = slow

        while forward is not None:
            if forward.val == reverse.val:
                forward = forward.next
                reverse = reverse.next
            else:
                return False

        return True

