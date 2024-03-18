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
    
    def node_at(self, head, idx):
        temp = head
        c = 0
        while temp!=None:
            if c==idx:
                return temp
            temp = temp.next
            c+=1
            
    def removeNthFromEnd(self, head, n):
        temp = head
        length = self.count(head)
        
        if length == 1 or length == n:
            return head.next
        
        target_idx = length - n - 1
        prev = self.node_at(head, target_idx)
        
        prev.next = prev.next.next
        
        return head