# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return 
        while head and head.next and head.val==head.next.val:
            VAL=head.val
            while head and head.val==VAL:
                head=head.next
                # print(head.val)
        else:
            Curr=head
            Length=0
            # print(Curr.val)
            OldCurr=ListNode(None)
            while Curr and Curr.next!=None:
                if Curr.val==Curr.next.val:
                    Length+=1
                    # print(Curr.val)
                    Val=Curr.val
                    while Curr and Curr.val==Val:
                        Curr=Curr.next
                    OldCurr.next=Curr
                    #print(OldCurr.next)
                else:
                    OldCurr=Curr
                    # print(OldCurr.val)
                    Curr=Curr.next
            if OldCurr!=None or Length==0:
                return head
            else:
                return OldCurr.val
