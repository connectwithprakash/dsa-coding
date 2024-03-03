# Palindrome Linked List

# Intuition
The idea is to find the median of the linked list which takes O(n) time. While finding the median, also reverse the first half of the linked list and get the two pointers in the middle to make the comparision for the palindrome.

# Approach
First we find the median using the two pointer approach where `slow` pointer increases position by one while the `fast` pointer increases position by two. With the loop condition, this helps us to find the median of the linked list. We instantiate the `reverse` variable with `None` and during each iteration of the while loop we attach `next` for the node to the `reverse` linked list. Hence, forming a reversed list.

We know that for an even number of elements, from the above algorithm, median is the second element but this element is in the second half. So, we instantiate `forward` with this node. And for odd number of elements, the median is right at the center, so, we instantiate `forward` with `next` node. The `reverse` variable is already set at right half because it stores the node previous to the median node.

Finally, we traverse through halves at the same time and compare each node's value. If there is a mismatch, the linked list is not a palindrome and we return `False` and if there is no mismatch, we return `True`.

# Complexity
- Time complexity: $$O(n/2)$$ -> $$O(n)$$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(1)$$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        reverse = None
        slow = fast = head
        # Reverse the first half till the median is found
        while (fast is not None) and (fast.next is not None):
            fast = fast.next.next
            # Reversing the first half
            temp = slow.next
            slow.next = reverse
            reverse = slow
            slow = temp
        # Instantiating forward pointer with appropriate start position
        if fast is not None:
            forward = slow.next
        else:
            forward = slow
        # Looping through halves using two pointers
        while forward is not None:
            if forward.val == reverse.val:
                forward = forward.next
                reverse = reverse.next
            else:
                return False

        return True
            
```
