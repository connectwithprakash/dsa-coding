# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        temp = result
        carry = 0
        time = 0
        while (l1 or l2):
            if l1 and l2:
                sum_ = l1.val + l2.val + carry
                l1 = l1.next
                l2 = l2.next
            elif l1:
                sum_ = l1.val + carry
                l1 = l1.next
            else:
                sum_ = l2.val + carry
                l2 = l2.next

            carry, ones = (sum_ // 10), (sum_ % 10)
            temp.next = ListNode(ones)
            temp = temp.next

        if carry:
            temp.next = ListNode(carry)

        return result.next


# Attempt 2: Add Two Numbers
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        head = result
        carry = 0
        while l1 or l2:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            
            carry, remainder = carry//10, carry%10
            head.next = ListNode(remainder)
            head = head.next

        while carry > 9:
            carry, remainder = carry//10, carry%10
            head.next = ListNode(remainder)
            head = head.next

        if carry:
            head.next = ListNode(carry)
            head = head.next

        return result.next

