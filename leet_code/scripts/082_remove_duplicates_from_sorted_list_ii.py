# Attempt 1: O(n) efficient solution

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Adding a dummy node before the head simplifies handling edge cases.
        head = ListNode(None, head)
        prev = head  # Pointer to the previous node
        curr = head.next  # Pointer to the current node

        repeat = False  # Flag to track if the current node's value is a duplicate
        while curr:
            # If the current node has a next node and they have the same value,
            # mark it as a repeat.
            if curr.next and (curr.val == curr.next.val):
                repeat = True
            # If the current node's value is a repeat, remove it by updating
            # the previous node's next pointer to skip over it.
            elif repeat:
                prev.next = curr.next
                repeat = False  # Reset the repeat flag
            else:
                prev = curr  # Move the previous pointer forward

            curr = curr.next  # Move the current pointer forward

        return head.next  # Return the head of the modified linked list

