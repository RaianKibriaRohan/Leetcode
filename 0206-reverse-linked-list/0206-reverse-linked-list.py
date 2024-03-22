# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def count(self,head):
        temp = head
        c = 0
        while temp!=None:
            c+=1
            temp = temp.next
        return c
    
    def node_at(self, head, index):
        temp = head
        c = 0
        while temp!=None:
            if c==index:
                return temp
            temp = temp.next
            c+=1
            
    def reverseList(self, head):
        temp = head
        dummy = ListNode() 
        current = dummy
        length = self.count(head)
        while length>0:
            getting = self.node_at(head,length-1)
            current.next = ListNode(getting.val)
            length-=1
            if length==0:
                break
            current = current.next

        return dummy.next
        