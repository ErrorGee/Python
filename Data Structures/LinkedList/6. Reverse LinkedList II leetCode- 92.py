# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head or left==right:
            return head
        Curr=head
        Length=0
        OldCurr=None
        while Curr:
            Prev=None
            Length+=1
            if Length==left:
                TailCurr=Curr
                while Length<=right:
                    Next=Curr.next
                    Curr.next=Prev
                    Prev=Curr
                    Curr=Next
                    Length+=1
                
                if OldCurr==None:
                    OldCurr=Prev
                    TailCurr.next=Curr
                    return Prev
                    
                TailCurr.next=Curr
                OldCurr.next=Prev
                return head
                
            else:
                OldCurr=Curr
                Curr=Curr.next
        return head
                    
                    
        
