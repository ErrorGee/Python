# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA==None or headB==None:
            return 0
        pointerA=headA
        pointerB=headB
        while (pointerA!=pointerB):
            if pointerA==None:
                pointerA=headB
            else:
                pointerA=pointerA.next
                
            if pointerB==None:
                pointerB=headA
            else:
                pointerB=pointerB.next
        return pointerB
            
        
                
                
            
        
