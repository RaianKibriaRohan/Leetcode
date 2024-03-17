# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        New = ListNode()
        moving = New
        temp1 = l1
        temp2 = l2
        carry = 0
        while temp1!=None or temp2!=None or carry!=0:
            if temp1!=None:
                v1 = temp1.val
            else:
                v1 = 0
                
            if temp2!=None:
                v2 = temp2.val
            else:
                v2 = 0
            
            Sum = v1+v2+carry #10
            carry = Sum//10   #1
            Sum %= 10         #0
            moving.next = ListNode(Sum)
            moving = moving.next
            
            if temp1!=None:            
                temp1 = temp1.next
            else:
                temp1 = None
            
            if temp2!=None:
                temp2 = temp2.next
            else:
                temp2 = None
            
        return New.next