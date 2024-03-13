# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        temp1 = list1
        temp2 = list2
        dummy = ListNode()
        tail = dummy
        while temp1!=None and temp2!=None:
            if temp1.val>temp2.val:
                tail.next = temp2
                temp2 = temp2.next
            else:
                tail.next = temp1
                temp1 = temp1.next
            
            tail = tail.next
            
        if temp1!=None:
            tail.next = temp1
        else:
            tail.next = temp2
        
        return dummy.next
        