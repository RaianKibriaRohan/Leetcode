# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def node_at(self, head, idx):
        temp = head
        c = 0
        while temp!=None:
            if c==idx:
                return temp
            temp = temp.next
            c+=1
    def mergeInBetween(self, list1, a, b, list2):
        temp1 = list1
        temp2 = list2
        get1 = self.node_at(list1, a-1)
        get2 = self.node_at(list1, b+1)
        get1.next = None
        get1.next = temp2
        while temp2!=None:
            if temp2.next==None:
                temp2.next = get2
                break
            temp2 = temp2.next
            
        return list1