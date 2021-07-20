"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head :
            return None
        PointerToCopy=head
        while PointerToCopy:
            NewNode=Node(PointerToCopy.val, PointerToCopy.next, None)
            PointerToCopy.next=NewNode
            PointerToCopy=NewNode.next
            
        PointerToSetRandom=head
        while PointerToSetRandom:
            if PointerToSetRandom.random!=None:
                PointerToSetRandom.next.random=PointerToSetRandom.random.next
            else:
                PointerToSetRandom.next.random=None
            PointerToSetRandom=PointerToSetRandom.next.next
                
        CopyList=head.next
        final_head=CopyList
        while CopyList:
            if CopyList.next!=None:
                CopyList.next=CopyList.next.next
            else:
                CopyList.next=None
            CopyList=CopyList.next
        return final_head
                
            
            
        
            
                
                
