# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        #two pointer approach
        DummyNode=ListNode(0)
        DummyNode.next=head
        Slow=DummyNode
        Fast=DummyNode
        for i in range(0, k):
            Fast=Fast.next
        First=Fast
        #print(First.val)
        while Fast!=None:
            Slow=Slow.next
            Fast=Fast.next
        Last=Slow
        #print(Last.val)
        Next=First.val
        First.val=Last.val
        Last.val=Next
        return DummyNode.next
        
             
