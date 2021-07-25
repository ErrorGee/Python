# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        Before=ListNode(-1)
        Before_head=Before
        After=ListNode(-1)
        After_head=After
        if not head:
            return head
        Curr=head
        while Curr:
            if Curr.val<x:
                Before.next=Curr
                Before=Before.next
            else:
                After.next=Curr
                After=After.next
            Curr=Curr.next
        After.next=None
        Before.next=After_head.next
        return Before_head.next
