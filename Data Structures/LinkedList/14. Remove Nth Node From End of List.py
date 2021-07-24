# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
      #using 2 pointers
        DummyNode=ListNode(0)
        DummyNode.next=head
        if not head:
            return head
        Slow=DummyNode
        Fast=DummyNode
        for i in range(0,n+1):
            Fast=Fast.next
        while Fast!=None:
            Slow=Slow.next
            Fast=Fast.next
        Slow.next=Slow.next.next
        return DummyNode.next
            
            
        
