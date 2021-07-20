# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return
        while (head and head.val==val):
            head=head.next
            
        Curr=head 
        while Curr and Curr.next!=None:
            if (Curr.next.val==val):
                Curr.next=Curr.next.next
            else:
                Curr=Curr.next
        return head
            
            
            
