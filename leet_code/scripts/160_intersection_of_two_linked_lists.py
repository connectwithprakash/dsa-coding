# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Naive solution: O(m+n+m)
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        temp1 = headA
        while temp1:
            temp1.val += 1e5
            temp1 = temp1.next
        temp2 = headB
        while temp2:
            if temp2.val > 1e5:
                break
            temp2 = temp2.next
        temp1 = headA
        while temp1:
            temp1.val -= 1e5
            temp1 = temp1.next
        
        if temp2:
            return temp2
        else:
            return None


# Better solution: O(m+n)
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
       temp1, temp2 = headA, headB
        while (temp1 is not temp2):
            if temp1:
                temp1 = temp1.next
            else:
                temp1 = headB
            if temp2:
                temp2 = temp2.next
            else:
                temp2 = headA

        return temp1

