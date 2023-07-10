# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

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

