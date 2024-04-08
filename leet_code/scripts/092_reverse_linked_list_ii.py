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


## Attempt 2: Using single pass through elements other than inside left and right
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        temp = head
        stack = []
        
        # get to the starting node that needs to be reversed
        for idx in range(2, left+1):
            temp = temp.next

        # Create a stack of the values to be reversed
        temp2 = temp
        for _ in range(left, right+1):
            stack.append(temp2.val)
            temp2 = temp2.next
        # Reverse the ordering from left to right
        for _ in range(left, right+1):
            temp.val = stack.pop()
            temp = temp.next
        
        return head

