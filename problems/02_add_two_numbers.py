# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(5)
        current_node = result
        carry = 0
        while True:
            x = y = 0
            if l1 == None and l2 == None:
                if carry != 0: 
                    current_node.next = ListNode(carry)
                return result.next
            
            if l1 != None:
                x = l1.val
                l1 = l1.next
            if l2 != None:
                y = l2.val
                l2 = l2.next
            
            s = x+y+carry
            print(x,y)
            new_node = ListNode(s%10)
            carry = s//10
            current_node.next = new_node
            current_node = new_node

        '''result = []
        carry = 0
        temp = l1
        while True:
            if l1 != None and l2 != None:
                sum = l1.val+l2.val+carry
                l1 = l1.next
                l2 = l2.next
            elif l1 == None and l2 != None:
                sum = l2.val+carry
                l2 = l2.next
            elif l1 != None and l2 == None:
                sum = l1.val+carry
                l2 = l1.next
            else:
                if carry != 0:
                    result.append(carry)
                break
            carry = sum//10
            result.append(sum%10)
        print(result)
        return temp.deserialize(str(result))'''
