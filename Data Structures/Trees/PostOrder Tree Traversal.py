#Task1: Post Order Traversal of Binary Tree
class NodeTree:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

def PostOrder(root):
    PostOrder=[]
    if not root:
        return PostOrder
    Stack=[]
    Curr=root
    while Stack or Curr:
        while Curr:
            Stack.append(Curr)
            Curr=Curr.left
        Temp=Stack[-1].right
        if Temp:
            Curr=Temp
        else:
            Temp=Stack.pop()
            PostOrder.append(Temp.val)
            while Stack and Temp==Stack[-1].right:
                Temp=Stack.pop()
                PostOrder.append(Temp.val)
    return PostOrder

if __name__=='__main__':
    root=NodeTree(1)
    root.left=NodeTree(9)
    root.right=NodeTree(2)
    root.right.left=NodeTree(3)
    root.right.left.left=NodeTree(4)
    root.right.left.right=NodeTree(5)
    print(PostOrder(root))

#Task 1 ends here .............................................................................

