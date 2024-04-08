## Attempt 1: Using two pass through the linkedlist

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        temp = head
        stack = []
        idx = 0
        while temp:
            idx += 1
            if left <= idx <= right:
                stack.append(temp.val)
            elif idx > right:
                break
            temp = temp.next
        
        temp = head
        idx = 0
        while temp:
            idx += 1
            if left <= idx <= right:
                temp.val = stack.pop()
            elif idx > right:
                break
            temp = temp.next

        return head

