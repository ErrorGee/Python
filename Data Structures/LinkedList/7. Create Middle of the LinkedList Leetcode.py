# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        Slow=head
        Fast=head
        while Fast!=None and Fast.next!=None:
            Slow=Slow.next
            Fast=Fast.next.next
        return Slow
            
        
