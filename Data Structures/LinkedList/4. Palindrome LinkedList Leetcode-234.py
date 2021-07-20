# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return False 
        Slow=head
        Fast=head
        while (Fast!=None and Fast.next!=None):
            Slow=Slow.next
            Fast=Fast.next.next
        Slow=self.reverse(Slow)
        Fast=head
        while(Slow!=None):
            if (Slow.val!=Fast.val):
                return False
            Slow=Slow.next
            Fast=Fast.next
            
        return True
    def reverse(self,head):
        Prev=None
        Curr=head
        while Curr:
            Next=Curr.next
            Curr.next=Prev
            Prev=Curr
            Curr=Next
        return Prev
        
        
        
        
