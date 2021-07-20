# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        Slow, Fast=head, head
        CyclePresent=False
        while(Fast and Fast.next):
            Slow=Slow.next
            Fast=Fast.next.next
            if Fast==Slow:
                CyclePresent=True
                break
        if CyclePresent==True:
            Slow,Index=head,0
            while(Slow!=Fast):
                Slow=Slow.next
                Fast=Fast.next
                Index+=1
            return Slow
            
            
