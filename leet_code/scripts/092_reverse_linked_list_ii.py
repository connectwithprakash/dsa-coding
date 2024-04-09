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


## Attempt 3: Single pass solution

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        # Helper function to reverse a portion of the linked list
        def reverse_left_right(node, steps):
            # Store the starting node of the reversed portion
            start = node
            # Initialize pointers for traversal and reversal
            curr = node
            prev = None
            # Iterate over the specified number of steps for reversal
            for idx in range(steps):
                # Store the next node temporarily
                temp = curr.next
                # Reverse the link
                curr.next = prev
                # Move pointers forward
                prev = curr
                curr = temp
            # Connect the start of the reversed portion to the next node after reversal
            start.next = curr
            # Return the new head of the reversed portion
            return prev

        # Create a dummy node and attach it to the head of the original linked list
        new_head = ListNode(0, head)
        # Initialize traversal pointer
        curr = new_head

        # Move the traversal pointer to the node before the left boundary
        for _ in range(left-1):
            curr = curr.next

        # Reverse the portion of the linked list from left to right
        curr.next = reverse_left_right(curr.next, right-left+1)

        # Return the head of the modified linked list
        return new_head.next

